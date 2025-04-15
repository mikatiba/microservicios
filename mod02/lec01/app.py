from flask import Flask, render_template

app = Flask(__name__)

#listas de los cursos y estudiantes
cursos = ['Matemáticas', 'Programación', 'Cultura', 'Física']
estudiantes = [
    {'nombre': 'Mikael', 'curso': 'Matemáticas'},
    {'nombre': 'Saúl', 'curso': 'Física'},
    {'nombre': 'Janiel', 'curso': 'Cultura'}
]
#ruta para el index
@app.route('/')
def index():
    return render_template('index.html')

#ruta para mostrar los cursos
@app.route('/cursos')
def mostrar_cursos():
    return render_template('cursos.html', cursos=cursos)

#mostrar estudiantes
@app.route('/estudiantes')
def mostrar_estudiantes():
    return render_template('estudiantes.html', estudiantes=estudiantes)

if __name__ == '__main__':
    app.run(debug=True)