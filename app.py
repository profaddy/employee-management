from flask import Flask;
from database.db import initialize_db;
from database.models import Employee;

from resources.employee import employees;

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/employee-management'
}

initialize_db(app);
app.register_blueprint(employees)


app.config['DEBUG'] = True
app.run()