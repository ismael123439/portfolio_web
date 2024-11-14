# app/models.py
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'  # Especifica explícitamente el nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.username}>'

    # Para evitar problemas de redefinición de tabla:
    __table_args__ = {'extend_existing': True}
