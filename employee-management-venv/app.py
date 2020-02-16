from flask import Flask, jsonify, request;
import uuid;

employees = [];
app = Flask(__name__)

@app.route('/')
def get_employees():
    return jsonify(employees);
 
@app.route('/employees', methods=['POST'])
def add_employee():
    employee = request.get_json();
    print ("add employee",employee);
    employee["id"] = uuid.uuid1()
    print("type>>>>>>>>>>>>>>.",type(employee['id']))
    employees.append(employee);
    return jsonify({"status":"true","length":len(employees),"response":employees[len(employees) - 1]}), 201;

@app.route('/employees/<id>', methods=['PUT'])
def update_employee(id):
    employee_data = request.get_json();
    employee_data["id"] = id;
    employee_index = 0
    for index in range(len(employees) - 1):
        if(employees[index]['id']) == id:
            employee_index = index
            employees[index] = employee_data
    return jsonify({"status":"true","length":len(employees),"response":employees[employee_index]}), 200;

@app.route('/employees/<id>',methods=['DELETE'])
def remove_employee(id):
    employee_index = 0
    for index in range(len(employees) - 1):
        if(str(employees[index]['id'])) == str(id):
            employee_index = index
            del employees[index];
    return jsonify({"status":"true","length":len(employees),"index":employee_index,"response":[]}), 201;

app.config['DEBUG'] = True
app.run()