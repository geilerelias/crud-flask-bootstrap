from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'


class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Text, nullable=True)
    sexo = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Persona {self.nombre}>'