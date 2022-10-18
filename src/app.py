from flask import Flask, render_template, redirect, url_for, flash, request, jsonify

from Modelos.Productos import ProductoSchema, Producto
from Config.Bd import app, db
from Modelos.Administrador import Administrador, AdministradorSchema
from Modelos.Carrito import Carrito, CarritoSchema
from Modelos.Cliente import Cliente, ClienteSchema


producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

@app.route('/', methods=['GET'])
def indexProducto():
    all_Productos = Producto.query.all()
    resultProductos = productos_schema.dump(all_Productos)
    #return render_template("Articulos/index.html",  articulos =resultArticulo)
    return jsonify(resultProductos) 

@app.route('/guardar', methods=['POST'])
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


@app.route('/<id>', methods=['GET'])
def buscar_producto(id):
    producto = Producto.query.get(id)
    return producto_schema.jsonify(producto)

@app.route('/<id>', methods=['PUT'])
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

@app.route('/<id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)

"""
@app.route('/dostablas', methods=['GET'])
def dostablas():
    results = db.session.query(Employee, Department).join(Department).all()    
    for employee, department in results:
        print(employee.name, department.name)
    return "dato"
"""
"""
@app.route('/trestablas',methods=['GET'])
def trestabla():
    results = db.session.query(Employee, Department, Company). \
    select_from(Employee).join(Department).join(Company).all()
    for employee, department, company in results:
        print(employee.name, department.name, company.name)
    return "Dato"
"""
"""
@app.route('/trestablaconfiltro', methods=['GET'])
def trestablaconfiltro():
    results = db.session.query(Employee.name, Employee.salary).join(Department).join(Company). \
    filter(Department.id == 1).all()

    for result in results:
        print(result)
    return 'Dato'
"""


#Iniciamos app para que se ejecute en un puerto#
if __name__ == "__main__":
    app.run(debug=True)
