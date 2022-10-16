
from codecs import CodecInfo
from Config.Bd import db, ma, app

class Productos(db.Model):
    __tablename__ = 'Producto'
    Cod = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Precio = db.Column(db.Float())
    PuntosC = db.Column(db.Float(50))#puntos de compra
    Tipo = db.Column(db.String(50))  #tipo de producto
    Imagen = db.Column(db.Blob())

    def __init__(self, Nombre, Precio, PuntosC, Tipo, Imagen):
        self.Nombre = Nombre
        self.Precio = Precio
        self.PuntosC = PuntosC
        self.Tipo = Tipo
        self.Imagen = Imagen
        
with app.app_context():
    db.create_all()


class ArticulosSchema(ma.Schema):
    class Meta:
        fields = ('Cod', 'Nombre', 'Precio', 'PuntosC', 'Tipo', 'Imagen')
