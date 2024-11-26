from flask import Flask

# Initialize Flask app
def create_app():
    app = Flask(__name__)

    # Import and register blueprints or routes
    from .proxy_api import app as proxy_app
    app.register_blueprint(proxy_app, url_prefix="/proxy-config")

    return app
