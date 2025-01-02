# backend/app/__init__.py
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Configuración básica
    app.config["SECRET_KEY"] = "your-secret-key"

    # Registrar las rutas
    from .routes import main_routes

    app.register_blueprint(main_routes)

    return app
