# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Usuario

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Crea una nueva instancia del usuario
        nuevo_usuario = Usuario(username=username, password=password)
        
        # Agrega y confirma el nuevo usuario en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        return redirect(url_for('index'))

    return render_template('registro.html')
