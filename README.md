# 🛡️ vuln-scanner

An advanced web vulnerability scanner for common security misconfigurations.

## 🔍 What It Does
This tool scans a given URL and checks for the presence of critical HTTP security headers:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Referrer-Policy`
- `Permissions-Policy`

Missing headers are flagged so developers can address them to improve web app security.

---

## 🌐 Now a Web App!
We recently upgraded this from a command-line script to a full **Flask web application** with:

- 🖥️ Simple UI form for URL input  
- 🚦 Live status and results display  
- 🚀 Auto-launch in browser on start  

---

## 🧪 Example Usage
1. Clone this repo
2. Run `app.py`
3. Your browser will auto-open to `http://127.0.0.1:5000`
4. Enter a URL and get instant scan results

---

## 📁 File Structure