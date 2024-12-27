from app import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":
    print("Servidor iniciado en http://127.0.0.1:5000")  # Confirmación de inicio
    serve(app, host='0.0.0.0', port=5000)

