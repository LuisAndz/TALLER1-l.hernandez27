from app.controllers.home_controller import home_bp

def registrar_rutas(app):
    app.register_blueprint(home_bp)