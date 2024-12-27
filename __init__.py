from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "¡Bienvenido a la API de predicción de pingüinos!"
    
    # Aquí podrías registrar otras rutas y configuraciones adicionales

    return app
