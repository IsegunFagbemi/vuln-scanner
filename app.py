from flask import Flask, request, render_template_string
import requests
import ssl
import socket
from datetime import datetime
from urllib.parse import urlparse

app = Flask(__name__)

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=10)
        missing = [header for header in SECURITY_HEADERS if header not in response.headers]
        return missing, None
    except Exception as e:
        return [], str(e)
    
def check_ssl_expiry(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname or parsed_url.path.split("/")[0]
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                expiry_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                days_left = (expiry_date - datetime.utcnow()).days
                if days_left <= 0:
                    return False, f"Certificate expired on {expiry_date}"
                else:
                    return True, f"Valid certificate (expires in {days_left} days)"
    except Exception as e:
        return False, f"SSL check failed: {e}"
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form.get("url")
        if not url.startswith("http"):
            url = "http://" + url  # Add http if user didn't

        missing, error = check_security_headers(url)
        ssl_valid, ssl_msg = check_ssl_expiry(url)
        result += f"<p><strong>SSL/TLS Check:<strong> {ssl_msg}</p>"

        if ssl_valid:
            result += f"<p style='color:green;'><strong>SSL/TLS Check:<strong> {ssl_msg}</p>"
        else:
            result += f"<p style='color:red;'><strong>SSL/TLS Check:<strong> {ssl_msg}</p>"

        if error:
            result = f"<p style='color:red;'>Error scanning URL: {error}</p>"
        elif missing:
            result = "<h3>Missing Security Headers:</h3><ul>"
            for header in missing:
                result += f"<li>{header}</li>"
            result += "</ul>"
        else:
            result = "<p style='color:green;'>All key security headers are present!</p>"

    return render_template_string("""
        <html>
            <head><title>Vulnerability Scanner</title></head>
            <body style="font-family:sans-serif; margin:40px;">
                <h1>Web Security Header Scanner</h1>
                <form method="post">
                    <label>Enter URL:</label>
                    <input type="text" name="url" required>
                    <button type="submit">Scan</button>
                </form>
                <div style="margin-top:20px;">{{ result|safe }}</div>
            </body>
        </html>
    """, result=result)

import threading
import webbrowser

if __name__ == "__main__":
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000")

    threading.Timer(1.0, open_browser).start()
    app.run(debug=True, use_reloader=False)
