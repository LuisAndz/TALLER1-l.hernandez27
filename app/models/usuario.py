from flask_login import UserMixin
from app.config.db import db


"""
Parte 1 - Punto 2 | Clase Usuario
Cree una clase usuario que tenga los atributos id, username y password. 
Dicha clase se usará para hacer las pruebas. Invéntese 3 usuarios cualquiera 
y cree instancias de estos.
"""

class Usuario(UserMixin, db.Model):
    
    __Tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)