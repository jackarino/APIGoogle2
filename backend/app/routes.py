import os
from dotenv import load_dotenv
from flask import Blueprint, jsonify

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

main_routes = Blueprint("main", __name__)


@main_routes.route("/")
def home():
    return jsonify({"message": "¡Bienvenido a la API con Flask!"})


def create_response(success, data=None, message=None):
    return jsonify({"success": success, "data": data, "message": message})


@main_routes.route("/get-api-key")
def get_api_key():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return create_response(False, message="Clave API no encontrada"), 500
    return create_response(True, data={"apiKey": api_key})


@main_routes.route("/docs")
def docs():
    return jsonify(
        {
            "/": "Endpoint de bienvenida",
            "/get-api-key": "Devuelve la clave API de Google Maps",
        }
    )
