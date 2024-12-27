import pytest
from app import create_app

# Fixture para inicializar la aplicación Flask
@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

# Prueba para la ruta de predicción
def test_predict(client):
    # Hacer una solicitud POST a la ruta '/predict'
    response = client.post('/predict', json={
        "culmen_length_mm": 50.0,
        "culmen_depth_mm": 15.0,
        "flipper_length_mm": 200.0,
        "body_mass_g": 5000,
        "island": "Biscoe",
        "sex": "male"
    })
    assert response.status_code == 200  # Verificar que el código de respuesta sea 200
    assert 'knn' in response.json       # Verificar que la predicción para el modelo KNN esté presente
