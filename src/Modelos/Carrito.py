
from Config.Bd import db, ma, app

class Carrito(db.Model):
    __tablename__ = 'Carrito'
    id = db.Column(db.Integer, primary_key=True)
    doc_cliente = db.Column(db.Integer, db.ForeignKey('Cliente.documento'))
    cantidad = db.Column(db.Integer)

    def __init__(self, id, doc_cliente, cantidad):
        self.id = id
        self.doc_cliente = doc_cliente
        self.cantidad = cantidad

with app.app_context():
    db.create_all()
    

class CarritoSchema(ma.Schema):
    class Meta:
        fields = ('id','doc_cliente', 'cantidad')
