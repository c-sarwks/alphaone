
from Config.Bd import db, ma, app
from Modelos.Usuario import Usuario

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    id = db.Column(db.Integer, primary_key = True)
    documento = db.Column(db.Integer)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    puntos = db.Column(db.Integer)
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(50))
    email_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id'))
  #  cod_usuario = db.Column(db.Integer, db.ForeignKey('Department.id'))
    
    salary = db.Column(db.Integer)

    def __init__(self, documento, nombre, apellidos, puntos, telefono, direccion, email_usuario):
        
        self.documento = documento
        self.nombre = nombre
        self.apellidos = apellidos
        self.puntos = puntos
        self.telefono = telefono
        self.direccion = direccion
        self.email_usuario = email_usuario

with app.app_context():
    db.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id','documento','nombre', 'apellidos', 'puntos', 'telefono', 'direccion', 'email_usuario')
