import requests

def scan_url(url):
    try:
        response = requests.get(url, timeout=10)
        print(f"Scannning {url} - Status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error scanning {url}: {e}")

if __name__ == "__main__":
    target = input("Enter URL to scan: ")
    scan_url(target)