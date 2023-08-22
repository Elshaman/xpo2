from app import db

class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=True)
    precio = db.Column(db.Numeric(precision=10, scale=2), nullable=True)
    imagen = db.Column(db.String(120), nullable=True)

