from app.config.db import db


class Cuidadores(db.Model):
    __Tablename__ = 'cuidadores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    id_guarderia = db.Column(db.Integer, nullable=False)
