# 🔍 Web Vulnerability Scanner

A lightweight Python-based web app for scanning security misconfigurations in websites — focused on missing HTTP security headers and SSL/TLS certificate validity.

## 🚀 Features
- Detects missing critical HTTP headers (e.g., CSP, HSTS, X-Frame-Options)
- Validates SSL/TLS certificate expiration and host matching
- Built with Flask – supports live URL scanning via a simple UI
- Automatically opens in browser when started
- Clear feedback on header status with error handling

## 🛠️ Technologies
- Python, Flask
- Requests, SSL
- HTML/CSS (via `render_template_string`)
- Git/GitHub

## 📸 Screenshot
![Screenshot](path_to_screenshot.png)

## 🧪 Try it locally
```bash
git clone https://github.com/yourusername/vulnerability-scanner.git
cd vulnerability-scanner
python app.py
