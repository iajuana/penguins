from app import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":
    # Usar Waitress en lugar de Gunicorn
    serve(app, host='0.0.0.0', port=5000)
