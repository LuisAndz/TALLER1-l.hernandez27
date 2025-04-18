from flask import Flask
from app.config.db import db
from app.models.usuario import Usuario
from app.models.crear_usuarios import crear_usuarios
# import app.models.crear_usuarios



def create_app(config) -> Flask:
    
    app = Flask(__name__, template_folder='views') # Se instancia la app
    app.config.from_object(config) # Recibe las variables de entorno
    db.init_app(app)
    
    
    with app.app_context():
        db.create_all()
        crear_usuarios()
        # nuevo_usuario = Usuario(usuario = 'david', contraseña='12345')
        # db.session.add(nuevo_usuario)
        # db.session.commit()
    
    
    return app