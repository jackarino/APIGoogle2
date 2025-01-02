# backend/app/routes.py
from flask import Blueprint, jsonify

main_routes = Blueprint("main", __name__)


@main_routes.route("/")
def home():
    return jsonify({"message": "¡Bienvenido a la API con Flask!"})
