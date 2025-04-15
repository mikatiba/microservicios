from flask_login import UserMixin

#usuarios
users = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user': {'password': 'user123', 'role': 'user'}
}

class User(UserMixin):
    def __init__(self, username, role):
        self.id = username
        self.role = role

    def set_password(self, password):
        # Aquí no hacemos hash ya que no usamos base de datos
        users[self.id]['password'] = password

    def check_password(self, password):
        return users.get(self.id, {}).get('password') == password