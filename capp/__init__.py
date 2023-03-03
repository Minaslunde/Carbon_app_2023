from flask import Flask
import os

application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']

application.config['SECRET_KEY'] = '9fc33e2141b285c7a608f746ad0ab0761678a42f146d4984'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

