from flask import Flask;
from flask_bcrypt import Bcrypt
from flask_restful import Api;
from database.db import initialize_db;
from resources.routes import initialize_routes;

app = Flask(__name__);

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/employee-management'
}
api = Api(app);
bcrypt = Bcrypt(app)
initialize_db(app);
initialize_routes(api);
app.config['DEBUG'] = True
app.run()