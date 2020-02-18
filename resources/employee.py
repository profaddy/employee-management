from flask import Flask, request, Response, jsonify,json,Blueprint
from database.db import initialize_db
from database.models import Employee

employees = Blueprint('employees', __name__);

@employees.route('/employees/')
def get_employees():
    id = request.args.get('id');
    if id is not None:
        employees = Employee.objects().get(id=id);
        response = {"status":"true","response":employees.to_json()}
    else:
        employees = Employee.objects();
        response = {"status":"true","length":employees.count(),"response":employees.to_json()}
    return Response(json.dumps(response), mimetype="application/json", status=200)
 
@employees.route('/employees', methods=['POST'])
def add_employee():
    body = request.get_json();
    employee = Employee(**body).save();
    # employees = Employee.objects().to_json();
    response = {"status":"true","response":employee}
    return Response(json.dumps(response), mimetype="application/json", status=201)

@employees.route('/employees/<id>', methods=['PUT'])
def update_employee(id):
    body = request.get_json();
    Employee.objects.get(id=id).update(**body)
    return '',200    

@employees.route('/employees/<id>',methods=['DELETE'])
def remove_employee(id):
    Employee.objects.get(id=id).delete();
    return '',200   
