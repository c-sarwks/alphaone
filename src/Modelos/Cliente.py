
from Config.Bd import db, ma, app
from Modelos.Usuario import Usuario

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    documento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    puntos = db.Column(db.Integer)
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(50))
  #  cod_usuario = db.Column(db.Integer, db.ForeignKey('Department.id'))
    
    salary = db.Column(db.Integer)

    def __init__(self, documento, nombre, apellidos, puntos, telefono, direccion):
        self.documento = documento
        self.nombre = nombre
        self.apellidos = apellidos
        self.puntos = puntos
        self.telefono = telefono
        self.direccion = direccion

with app.app_context():
    db.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('documento','nombre', 'apellidos', 'puntos', 'telefono', 'direccion')
