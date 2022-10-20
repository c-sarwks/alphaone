from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from Modelos.Producto import ProductoSchema, Producto
from Config.Bd import app, db
from Toke import *
import json
#from Modelos.Administrador import Administrador, AdministradorSchema
from Modelos.Carrito import Carrito, CarritoSchema
from Modelos.Cliente import Cliente, ClienteSchema
from Modelos.Usuario import Usuario, UsuarioSchema



producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)
usuario_schema = UsuarioSchema()
cliente_schema = ClienteSchema()
carrito_schema = CarritoSchema()

@app.route('/Product', methods=['GET'])
def buscarProductos():
    all_Productos = Producto.query.all()
    resultProductos = productos_schema.dump(all_Productos)
    #return render_template("Articulos/index.html",  articulos =resultArticulo)
    return jsonify(resultProductos) 

@app.route('/Product/guardar', methods=['POST'])
def agregar_producto():
    Nombre = request.json['Nombre']
    Precio = request.json['Precio']
    PuntosC = request.json['PuntosC']
    Tipo = request.json['Tipo']
    Imagen = request.json['Imagen']

    new_producto = Producto(Nombre, Precio, PuntosC, Tipo, Imagen)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)


@app.route('/Product/<id>', methods=['GET'])
def buscar_producto(id):
    producto = Producto.query.get(id)
    return producto_schema.jsonify(producto)

@app.route('/Product/<id>', methods=['PUT'])
def editar_producto(id):
    producto = Producto.query.get(id)
    Nombre = request.json['Nombre']
    Precio = request.json['Precio']
    PuntosC = request.json['PuntosC']
    Tipo = request.json['Tipo']
    Imagen = request.json['Imagen']
    
    producto.Nombre = Nombre
    producto.Precio = Precio
    producto.PuntosC = PuntosC
    producto.Tipo = Tipo
    producto.Imagen = Imagen
    db.session.commit()
    return producto_schema.jsonify(producto)

@app.route('/Product/<id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)

@app.route('/Product/Descuento/<id>', methods=['POST'])
def producto_descuento(id):
    producto = Producto.query.get(id)
    descuento = request.json['Descuento']
    newPrecio = producto.Precio-(producto.Precio*descuento)  #Descuento es un porcentaje
    return {"Precio_Descuento":newPrecio}

@app.route('/auth/guardar', methods=['POST'])
def registrar_usuario():
    email = request.json['email']
    contraseña = request.json['contraseña']
    rol = request.json['rol']

    new_usuario = Usuario(email, contraseña, rol)
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)

@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    contraseña = request.json['contraseña']
    usuario = Usuario.query.filter_by(email=email).first()

    if usuario==None:
        return {
            "Mensaje": "El usuario no existe"
        }

    if usuario.email==email and usuario.contraseña==contraseña:
        token = generar_token(usuario.email, usuario.contraseña)
        resultUser = usuario_schema.dump(usuario)
        del resultUser['contraseña']
        return {
            "mensaje":"Has iniciado sesión",
            "token": token,
            "usuario": resultUser
        }
    else:
        return {"Mensaje":"Inicio de sesión denegado"}

@app.route('/Client/guardar', methods=['POST'])
def agregar_Cliente():
    documento = request.json['documento']
    nombre = request.json['nombre']
    apellidos = request.json['apellidos']
    puntos = request.json['puntos']
    telefono = request.json['telefono']
    direccion = request.json['direccion']
    id_usuario = request.json['Usuario.id']

    new_cliente = Cliente(documento, nombre, apellidos, puntos, telefono, direccion, id_usuario)
    db.session.add(new_cliente)
    db.session.commit()
    return cliente_schema.jsonify(new_cliente)

@app.errorhandler(400)
def error1(e):
    return {"StatusCode":"Error 400"}

@app.errorhandler(404)
def error2(e):
    return {"StatusCode":"Error 404"}   

@app.errorhandler(405)
def error(e):
    return {"StatusCode":"Error 405"}

#Iniciamos app para que se ejecute en un puerto#
if __name__ == "__main__":
    app.run(debug=True)
