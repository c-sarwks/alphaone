
from codecs import CodecInfo
from Config.Bd import db, ma, app

class Producto(db.Model):
    __tablename__ = 'Producto'
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Precio = db.Column(db.Float)
    PuntosC = db.Column(db.Integer)#puntos de compra
    Tipo = db.Column(db.String(50))  #tipo de producto
    Imagen = db.Column(db.Blob)

    def __init__(self, Nombre, Precio, PuntosC, Tipo, Imagen):
        self.Nombre = Nombre
        self.Precio = Precio
        self.PuntosC = PuntosC
        self.Tipo = Tipo
        self.Imagen = Imagen
        
with app.app_context():
    db.create_all()


class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'Nombre', 'Precio', 'PuntosC', 'Tipo', 'Imagen')
