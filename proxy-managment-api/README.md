Deployment steps:

Image build and compose (bash):
docker build -t proxy-api .

Running container (bash):
docker run -d -p 5000:5000 --env-file .env proxy-api

# Proxy Management API

A Flask-based API to manage proxy configurations using the Webshare API.

## Features
- **Fetch Proxies**: Retrieve all proxies.
- **Update Configuration**: Change username/password.
- **Download Proxies**: Export a list of proxies in CSV format.

## Setup
### Prerequisites
- Docker
- Python 3.9+

### Installation
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd proxy-management-api
