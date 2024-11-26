from flask import Flask, jsonify, request, send_file
import requests
from io import StringIO
from config import API_URL, API_KEY

app = Flask(__name__)

# Fetch proxy configurations
@app.route('/proxy-config', methods=['GET'])
def get_proxy_config():
    headers = {"Authorization": f"Token {API_KEY}"}
    response = requests.get(f"{API_URL}/proxy/list/", headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Failed to fetch proxy config"}), response.status_code

# Update proxy username or password
@app.route('/proxy-config', methods=['PATCH'])
def patch_proxy_config():
    headers = {"Authorization": f"Token {API_KEY}"}
    patch_data = request.json
    response = requests.patch(f"{API_URL}/proxy/config/", json=patch_data, headers=headers)
    if response.status_code in [200, 204]:
        return jsonify({"message": "Proxy configuration updated successfully."})
    return jsonify({"error": "Failed to update proxy config"}), response.status_code

# Download all proxies as a list
@app.route('/proxy-config/download', methods=['GET'])
def download_proxies():
    headers = {"Authorization": f"Token {API_KEY}"}
    response = requests.get(f"{API_URL}/proxy/list/", headers=headers)
    if response.status_code == 200:
        proxies = response.json().get('results', [])
        csv_content = "IP:Port,Username,Password\n"
        for proxy in proxies:
            csv_content += f"{proxy['ip']}:{proxy['port']},{proxy['username']},{proxy['password']}\n"
        csv_file = StringIO(csv_content)
        csv_file.seek(0)
        return send_file(
            csv_file,
            as_attachment=True,
            download_name="proxies.csv",
            mimetype="text/csv"
        )
    return jsonify({"error": "Failed to fetch proxies for download"}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
