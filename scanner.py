import requests


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
        return [header for header in SECURITY_HEADERS if header not in response.headers], None
    except Exception as e:
        return [], str(e)

def scan_url(url):
    try:
        response = requests.get(url, timeout=10)
        print(f"Scanning {url} - Status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error scanning {url}: {e}")
        return

    print(f"Scanning {url}...")
    missing_headers, error = check_security_headers(url)

    if error:
        print(f"Error during header check: {error}")
    elif missing_headers:
        print("Missing Security Headers:")
        for header in missing_headers:
            print(f"- {header}")
    else:
        print("All key security headers are present.")

if __name__ == "__main__":
    target = input("Enter URL to scan: ")
    scan_url(target)



    
