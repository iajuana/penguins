from flask import Flask

def create_app():
    """Función para crear e inicializar la aplicación Flask."""
    
    # Crear la aplicación Flask
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object('app.config.Config')
    
    # Registrar Blueprints (modulos de la aplicación)
    from app.main import main_bp
    app.register_blueprint(main_bp)
    
    return app
