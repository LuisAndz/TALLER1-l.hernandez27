from flask_login import LoginManager
from app.models.usuario import Usuario


"""
    Parte 1 - Punto 3 | Autenticación
    Implemente un módulo de autenticación según lo descrito en las diapositivas. 
"""

login_manager = LoginManager() # Genera un objeto LoginManager

@login_manager.user_loader
def load_user(user_id: str) -> Usuario:
    
    try:
        user = Usuario.query.get(str(user_id))
        print("Ok user")
        return user
    except Exception as e:
        print (f"Error al cargar el usuario: {e}")
        return None