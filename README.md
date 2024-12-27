# Proyecto de clasificación de pingüinos

Este proyecto utiliza modelos de aprendizaje automático para predecir la especie de un pingüino basada en características como el tamaño del pico, la longitud de la aleta, y el peso corporal. El modelo está desplegado como una API REST utilizando Flask.

## Requisitos

- **Flask**: Framework de Python para la creación de la API.
- **Poetry**: Herramienta para la gestión de dependencias y entornos virtuales.
- **Scikit-learn**: Librería para crear y entrenar los modelos de machine learning.
- **Waitress**: Servidor WSGI para ejecutar la aplicación en producción.


- Python 3.12 o superior
- Poetry (para gestionar las dependencias)

### Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/iajuana/penguins.git

2. Navega al directorio del proyecto:
cd penguins
3. Instala las dependencias utilizando Poetry:
poetry install
4. Ejecuta el proyecto:
poetry run python main.py
