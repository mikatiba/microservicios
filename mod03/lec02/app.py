from flask import Flask, redirect, url_for, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_principal import Principal, Permission, RoleNeed, Identity, identity_changed, identity_loaded, AnonymousIdentity

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Necesario para sesiones

# Inicializar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Inicializar Flask-Principal
principals = Principal(app)

# Definimos roles
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))
guest_permission = Permission(RoleNeed('guest'))

# Simulamos usuarios (base de datos en memoria)
users = {
    'admin': {'password': 'admin', 'roles': ['admin']},
    'user': {'password': 'user', 'roles': ['user']},
    'guest': {'password': 'guest', 'roles': ['guest']}
}

# Modelo de Usuario
class User(UserMixin):
    def __init__(self, id, roles):
        self.id = id
        self.roles = roles

# Cargar usuario
@login_manager.user_loader
def load_user(user_id):
    user = users.get(user_id)
    if user:
        return User(user_id, user['roles'])
    return None

# Login de prueba
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = users.get(username)

    if user and user['password'] == password:
        user_obj = User(username, user['roles'])
        login_user(user_obj)
        identity_changed.send(app, identity=Identity(user_obj.id))
        return jsonify(message=f"Logged in as {username}")
    return jsonify(message="Invalid credentials"), 401

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    return jsonify(message="Logged out")

# Ruta solo para Admin
@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin_route():
    return jsonify(message="Welcome Admin!")

# Ruta para usuarios normales
@app.route('/user')
@login_required
@user_permission.require(http_exception=403)
def user_route():
    return jsonify(message="Welcome User!")

# Ruta para invitados
@app.route('/guest')
@login_required
@guest_permission.require(http_exception=403)
def guest_route():
    return jsonify(message="Welcome Guest!")

# Cargar roles en identidad
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role))

if __name__ == '__main__':
    app.run(debug=True)
