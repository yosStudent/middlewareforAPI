import requests
from config import API_URL, API_KEY

# Utility function to make GET requests to the root service API
def fetch_proxies():
    headers = {"Authorization": f"Token {API_KEY}"}
    response = requests.get(f"{API_URL}/proxy/list/", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch proxies", "status_code": response.status_code}

# Utility function to patch proxy configuration
def update_proxy_config(data):
    headers = {"Authorization": f"Token {API_KEY}"}
    response = requests.patch(f"{API_URL}/proxy/config/", json=data, headers=headers)
    return {
        "status_code": response.status_code,
        "message": "Success" if response.status_code in [200, 204] else "Failed",
    }

# Utility function to download proxies in CSV format
def generate_csv(proxies):
    csv_content = "IP:Port,Username,Password\n"
    for proxy in proxies:
        csv_content += f"{proxy['ip']}:{proxy['port']},{proxy['username']},{proxy['password']}\n"
    return csv_content
