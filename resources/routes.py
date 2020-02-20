from .employee import EmployeesApi, EmployeeApiwithId;
from .auth import SignupApi;

def initialize_routes(api):
 api.add_resource(EmployeesApi, '/api/v1/employees');
 api.add_resource(EmployeeApiwithId, 'api/v1/employees/<id>');
 api.add_resource(SignupApi, 'api/auth/signup')