from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de usuarios en memoria
usuarios = []

# Ruta: GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "sistema": "Gestor de productos y usuarios",
        "versión": "1.0",
        "autor": "Mikael Tiba"
    }), 200

# Ruta: POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data.get("nombre")
    correo = data.get("correo")

    if not nombre or not correo:
        return jsonify({"error": "Faltan datos: nombre y correo son requeridos."}), 400

    usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(usuario)
    return jsonify({"mensaje": "Usuario creado correctamente", "usuario": usuario}), 201

# Ruta: GET /usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios}), 200

if __name__ == "__main__":
    app.run(debug=True)