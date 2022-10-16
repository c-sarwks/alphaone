from flask import Flask,render_template, redirect, url_for, flash, request, jsonify

from Modelos.Articulos import ArticulosSchema, Articulo
from Config.Bd import app, db
from Modelos.Company import Company, CompanySchema
from Modelos.Department import Department, DepartmentSchema
from Modelos.Employee import Employee, EmployeeSchema


articulo_schema = ArticulosSchema()
articulos_schema = ArticulosSchema(many=True)

@app.route('/', methods=['GET'])
def indexArticulo():
    all_articulos = Articulo.query.all()
    resultArticulo = articulos_schema.dump(all_articulos)
    #return render_template("Articulos/index.html",  articulos =resultArticulo)
    return jsonify(resultArticulo) 

@app.route('/guardar', methods=['POST'])
def save():
    Nombre = request.json['Nombre']
    Precio = request.json['Precio']

    new_articulo = Articulo(Nombre, Precio)
    db.session.add(new_articulo)
    db.session.commit()
    return articulo_schema.jsonify(new_articulo)


@app.route('/<id>', methods=['GET'])
def get_one_articulo(id):
    articulo = Articulo.query.get(id)
    return articulo_schema.jsonify(articulo)

@app.route('/<id>', methods=['PUT'])
def update_articulo(id):
    articulo = Articulo.query.get(id)
    Nombre = request.json['Nombre']
    Precio = request.json['Precio']
    
    articulo.Nombre = Nombre
    articulo.Precio = Precio
    db.session.commit()
    return articulo_schema.jsonify(articulo)

@app.route('/<id>', methods=['DELETE'])
def Delete_articulo(id):
    articulo = Articulo.query.get(id)
    db.session.delete(articulo)
    db.session.commit()
    return articulo_schema.jsonify(articulo)

@app.route('/dostablas', methods=['GET'])
def dostablas():
    results = db.session.query(Employee, Department).join(Department).all()    
    for employee, department in results:
        print(employee.name, department.name)
    return "dato"
    

@app.route('/trestablas',methods=['GET'])
def trestabla():
    results = db.session.query(Employee, Department, Company). \
    select_from(Employee).join(Department).join(Company).all()
    for employee, department, company in results:
        print(employee.name, department.name, company.name)
    return "Dato"

@app.route('/trestablaconfiltro', methods=['GET'])
def trestablaconfiltro():
    results = db.session.query(Employee.name, Employee.salary).join(Department).join(Company). \
    filter(Department.id == 1).all()

    for result in results:
        print(result)
    return 'Dato'


#Iniciamos app para que se ejecute en un puerto#
if __name__ == "__main__":
    app.run(debug=True)
