from flask import Flask, jsonify, request

app = Flask(__name__)

todos = {
          "todos": ['Estudiar', 'Comer', 'Jugar UNO'] #lista de los todos
        }

@app.route("/todos", methods=["GET"]) #ruta que devuelve la lista de todos en JSON
def select_todos():
        return jsonify(todos)

@app.route("/todos", methods=["POST"]) 
def create_todo():
    data = request.json
    if not data or "todo" not in data:
        return jsonify({"error": "Datos incompletos"}), 400 #devuelve error

    todos["todos"].append(data['todo']) #añade todo

    return jsonify({"message": "Nuevo todo creado"}), 200 #indica que se creo un todo

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)


