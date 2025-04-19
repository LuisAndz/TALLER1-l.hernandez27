from app.config.db import db
from app.models.usuario import Usuario
from app.models.perros import Perros
from app.models.guarderias import Guarderias
from app.models.cuidadores import Cuidadores

def crear_usuarios():
    usuarios = [
        {'username': 'andres', 'password': 'neo123', 'es_admin':'1'},
        {'username': 'martha', 'password': 'mad12345', 'es_admin':'0'},
        {'username': 'david', 'password': '12345', 'es_admin':'0'}
    ]

    try:
        for u in usuarios:
            nuevo_usuario = Usuario(username=u['username'], password=u['password'], es_admin=u['es_admin'])
            db.session.add(nuevo_usuario)
        
        db.session.commit()
        print("Usuarios creados correctamente")

    except Exception as e:
        print(f"Error creando usuarios: {e}")
        db.session.rollback()

def mostrar_perros():
    perros = db.session.query(
        Perros,
        Cuidadores.nombre.label('cuidador'),
        Guarderias.nombre.label('guarderia')
    ).join(
        Cuidadores, Perros.id_cuidador == Cuidadores.id
    ).join(
        Guarderias, Perros.id_guarderia == Guarderias.id
    ).all()
    return perros

def limpiar_tablas(app):
        with app.app_context():
            db.session.query(Usuario).delete()
            db.session.commit()
            print("Tablas limpias")