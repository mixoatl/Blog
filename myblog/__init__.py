from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)

#Cargar las configuraciones
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

#Importar vistas 
from myblog.views.auth import auth
from myblog.views.admin import admin as admin_blueprint
app.register_blueprint(auth)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

from myblog.views.blog import blog
app.register_blueprint(blog)
app.add_url_rule('/', endpoint='index')

with app.app_context():
    db.create_all()
