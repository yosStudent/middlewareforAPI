import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_proxy_config(client, mocker):
    # Mock the root service API response
    mock_response = {"results": [{"ip": "127.0.0.1", "port": "8080", "username": "user", "password": "pass"}]}
    mocker.patch("app.utils.fetch_proxies", return_value=mock_response)

    response = client.get("/proxy-config")
    assert response.status_code == 200
    assert response.json == mock_response

def test_patch_proxy_config(client, mocker):
    # Mock the root service API patch response
    mock_response = {"message": "Success"}
    mocker.patch("app.utils.update_proxy_config", return_value=mock_response)

    response = client.patch("/proxy-config", json={"username": "new_user"})
    assert response.status_code == 200
    assert response.json["message"] == "Proxy configuration updated successfully."

def test_download_proxies(client, mocker):
    # Mock proxy list for download
    mock_proxies = [
        {"ip": "127.0.0.1", "port": "8080", "username": "user", "password": "pass"}
    ]
    mocker.patch("app.utils.fetch_proxies", return_value={"results": mock_proxies})

    response = client.get("/proxy-config/download")
    assert response.status_code == 200
    assert "text/csv" in response.content_type
    assert "IP:Port,Username,Password" in response.get_data(as_text=True)
