from app.config.db import db
from app.models.usuario import Usuario

def crear_usuarios():
    usuarios = [
        {'username': 'andres', 'password': 'neo123'},
        {'username': 'martha', 'password': 'mad12345'},
        {'username': 'david', 'password': '12345'}
    ]

    try:
        for u in usuarios:
            nuevo_usuario = Usuario(username=u['username'], password=u['password'])
            db.session.add(nuevo_usuario)
        
        db.session.commit()
        print("Usuarios creados correctamente")

    except Exception as e:
        print(f"Error creando usuarios: {e}")
        db.session.rollback()
