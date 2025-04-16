from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta'

@app.route('/register', methods=['GET', 'POST']) 
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Usuario registrado exitosamente!', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)