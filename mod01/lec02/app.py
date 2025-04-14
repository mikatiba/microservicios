from flask import Flask, request, jsonify

app = Flask(__name__)

nombres_lista = ["Mikael", "Saúl", "Janiel"] #Lista con nombres

@app.route('/nombres', methods=["GET", "POST"])
def nombres():
    if request.method=="GET": #Si se hace un request GET devuelve la lista con nombres
        return{"nombres": nombres_lista}

    if request.method=="POST": #Si se hace un request POST añade el nombre a la lista

        data = request.get_json()
        nuevo_nombre = data.get("nombre")
       
        if nuevo_nombre:
            nombres_lista.append(nuevo_nombre) #añade nombre a la lista
            return jsonify({"mensaje": f"El nombre {nuevo_nombre} ha sido añadido"}), 201
        else:
            return jsonify({"error": "Debes enviar un nombre en el JSON"}), 400

       
if __name__ == "__main__":
    app.run(debug=True)

