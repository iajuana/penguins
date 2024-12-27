# Proyecto de clasificación de pingüinos

Este proyecto utiliza diversos modelos de clasificación para predecir la especie de pingüino a partir de datos de características como la longitud del pico, la profundidad del pico, el tamaño de las aletas, etc.

## Requisitos

- Flask
- joblib
- seaborn
- scikit-learn

## Instrucciones de instalación

1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta `python model_training.py` para entrenar y guardar los modelos.
4. Ejecuta `python main.py` para iniciar el servidor Flask.
5. Realiza peticiones POST a `http://127.0.0.1:5000/predict` con los datos de entrada para obtener predicciones.

