from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import User, users

app = Flask(__name__)
app.secret_key = 'supersecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Función para cargar al usuario desde el diccionario
@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id, users[user_id]['role'])
    return None

@app.route('/')
def index():
    return redirect(url_for('login')) #te lleva al login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        
        #si el usuario existe te envía al dashboard
        user_data = users.get(username)
        if user_data and user_data['password'] == password:
            user = User(username, user_data['role'])
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash("Credenciales inválidas") #si el usuario no existe imprime este mensaje
    return render_template('login.html')

@app.route('/dashboard') #te envía al dashboard
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/logout') #una vez le des click a "logout" te envía a la página de login
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)