from flask import Flask
from app.routes import main_routes
from config import Config
from flask_cors import CORS
import os

if not os.getenv("GOOGLE_API_KEY"):
    raise EnvironmentError("GOOGLE_API_KEY no está configurada en el archivo .env")


app = Flask(__name__)
app.config.from_object(Config)

### production : CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://tu-dominio.com"]}})
### development : CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})

# Registrar las rutas
app.register_blueprint(main_routes)

if __name__ == "__main__":
    app.run(debug=True)
