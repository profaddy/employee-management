from flask import request,jsonify;
from flask_restful import Resource;
from database.models import User;

class SignupApi(Resource):
    def post(self):
        body = request.get_json();
        user = User(**body);
        user.hash_password();
        user.save();
        id = user.id
        return {"status":"true",'id': str(id)}, 200