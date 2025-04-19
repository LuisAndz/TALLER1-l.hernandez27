from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from app.models.usuario import Usuario
from app.models.funciones_tablas import mostrar_perros

home_bp = Blueprint("home", __name__)

@home_bp.route('/', methods = ['GET'])
def home():
    return render_template('index.html')


@home_bp.route('/login', methods = ['GET', 'POST'])
def login():
    
    if request.method == 'GET': # Si carga la pagina por 1ra vez, muestre login.html
        return render_template('login.html')
    
    elif request.method == 'POST': # Si es un POST, consulte....
        username = request.form.get('username')
        password = request.form.get('password')
        
        usuario = Usuario.query.filter_by(username=username, password=password).first()
        
        """
            Parte 1 - Punto 3 | Autenticación
            Cuando se logre iniciar sesión, muestre un mensaje de saludo como el que 
            aparece en las diapositivas, puede agregarle más cosas a esta vista si lo desea.
        """
        if(usuario):
            login_user(usuario) # Loguea el usuario
            
            if usuario.es_admin == 1:
                return redirect(url_for("home.dashboard_admin"))#Si admin vamos al panel de admin
            else:
                return redirect(url_for('home.dashboard'))
        
        #Si no encuentra al usuario retorna al login
        flash("Las credenciales son incorrectas.", "danger")
        return redirect(url_for("home.login"))

@home_bp.route('/dashboard', methods = ['GET'])
@login_required
def dashboard():
    username = current_user.username
    return render_template('dashboard.html', username = username)

@home_bp.route('/dashboard_admin', methods = ['GET'])
@login_required
def dashboard_admin():
    username = current_user.username
    perros=mostrar_perros()
    return render_template('dashboard_admin.html', username = username, perros = perros)

@home_bp.route('/logout', methods = ['GET'])
def logout():
    logout_user()
    return redirect(url_for("home.login"))