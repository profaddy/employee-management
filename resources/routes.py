from .employee import EmployeesApi, EmployeeApiwithId;

def initialize_routes(api):
 api.add_resource(EmployeesApi, '/employees')
 api.add_resource(EmployeeApiwithId, '/employees/<id>')