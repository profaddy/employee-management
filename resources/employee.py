from flask import Flask, request, Response, jsonify,json
from flask_restful import Resource
from database.models import Employee


class EmployeesApi(Resource):
    def get(self):
        employees = Employee.objects();
        response = {"status":"true","length":employees.count(),"response":employees.to_json()}
        return Response(json.dumps(response), mimetype="application/json", status=200)
    def  post(self):
        body = request.get_json();
        employee = Employee(**body).save();
        response = {"status":"true","response":employee}
        return Response(json.dumps(response), mimetype="application/json", status=201)

class EmployeeApiwithId(Resource):
    def get(self,id):
        employees = Employee.objects().get(id=id);
        response = {"status":"true","response":employees.to_json()} ;
        return Response(json.dumps(response), mimetype="application/json", status=200)
    def put(self,id):
        body = request.get_json();
        Employee.objects.get(id=id).update(**body)
        return '',200    

    def delete(self,id):
        Employee.objects.get(id=id).delete();
        return '',200   
