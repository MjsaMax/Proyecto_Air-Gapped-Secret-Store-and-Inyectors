import os
import sys
from flask import flask
app = Flask(__name__)

@app.route('/')
def home():
    # Intenta leer el secreto de las variables de entorno
    secret = os.getenv("API_TOKEN")
    
    if secret:
        return f"Conexión exitosa al servicio interno simulado. Token recibido."
    else:
        return "Error: No se encontró la variable API_TOKEN. Acceso denegado."

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)