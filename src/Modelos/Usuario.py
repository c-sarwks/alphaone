from Config.Bd import db, ma, app

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))
    rol = db.Column(db.String(50))

    def __init__(self, email, contraseña, rol):
        self.email = email
        self.contraseña = contraseña
        self.rol = rol

with app.app_context():
    db.create_all()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id','email', 'contraseña', 'rol')