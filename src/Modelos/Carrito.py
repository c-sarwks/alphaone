
from Config.Bd import db, ma, app
from Modelos.Cliente import Cliente

class Carrito(db.Model):
    __tablename__ = 'Carrito'

    id = db.Column(db.Integer, primary_key=True)
    doc_cliente = db.Column(db.Integer, db.ForeignKey('Cliente.id'),nullable=True)
    cantidad = db.Column(db.Integer)

    def __init__(self, doc_cliente, cantidad):
        self.doc_cliente = doc_cliente
        self.cantidad = cantidad

with app.app_context():
    db.create_all()
    

class CarritoSchema(ma.Schema):
    class Meta:
        fields = ('id','Cliente.id', 'cantidad')
