my_flask_api/
│
├── models/                    # Modelos entrenados y preprocesadores
│   ├── knn_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── decision_tree_model.pkl
│   ├── random_forest_model.pkl
│   └── preprocessor.pkl        # Preprocesador guardado
│
├── app/                        # Código de la API Flask
│   ├── __init__.py             # Inicialización de la aplicación Flask
│   ├── main.py                 # Código principal de la API Flask
│   └── config.py               # Configuración de la API
│
├── tests/                      # Pruebas unitarias y de integración
│   └── test_main.py            # Pruebas para la API
│
├── Dockerfile                  # Dockerfile para contenerizar la aplicación
├── requirements.txt            # Dependencias de Python
└── README.md                   # Documentación básica del proyecto
