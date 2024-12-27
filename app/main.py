import pickle
from flask import Blueprint, request, jsonify
import pandas as pd




# Crear el blueprint para las rutas principales
main_bp = Blueprint('main', __name__)

@main_bp.route('/predict', methods=['POST'])
def predict():
    """Recibe los datos y hace una predicción utilizando los modelos entrenados."""
    try:
        # Obtener los datos JSON de la solicitud POST
        data = request.get_json()
        
        # Convertir los datos JSON a un DataFrame de pandas
        data_df = pd.DataFrame([data])
        
        # Cargar el preprocesador guardado (para transformar las características)
        with open('models/preprocessor.pkl', 'rb') as f:
            preprocessor = pickle.load(f)
        
        # Preprocesar los datos de entrada
        processed_data = preprocessor.transform(data_df)
        
        # Diccionario para almacenar las predicciones de cada modelo
        predictions = {}
        
        # Iterar sobre cada modelo y hacer la predicción
        for model_name in ['knn', 'logistic_regression', 'decision_tree', 'random_forest']:
            with open(f'models/{model_name}_model.pkl', 'rb') as f:
                model = pickle.load(f)
            prediction = model.predict(processed_data)
            predictions[model_name] = prediction[0]  # Guardar solo la primera predicción
        
        # Retornar las predicciones como un JSON
        return jsonify(predictions)
    
    except Exception as e:
        # Manejo de errores en caso de que ocurra un fallo
        return jsonify({"error": str(e)}), 400
