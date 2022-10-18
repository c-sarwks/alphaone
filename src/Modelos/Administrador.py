from Config.Bd import db, ma, app
from Modelos.Usuario import Usuario

class Administrador(db.Model):
    __tablename__ = 'Administrador'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, id, name):
        self.id = id
        self.name = name

with app.app_context():
    db.create_all()

class AdministradorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
