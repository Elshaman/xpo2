from app import db

class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer , primary_key = True)

