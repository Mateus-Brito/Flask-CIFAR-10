import os

from flask import Flask

from app.views import cifar_browser


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config["UPLOADED_PATH"] = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "uploaded"
    )
    app.config["models"] = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "models"
    )
    app.url_map.strict_slashes = False
    app.register_blueprint(cifar_browser)
    return app
