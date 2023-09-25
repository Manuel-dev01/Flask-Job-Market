from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# db = SQLAlchemy()
# DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'HDJDSOSOP'
    # app.config['SQLAlchemy_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # db.init_app(app)

    from .auth import auth 
    from .views import views

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')


    # if not path.exists('website/' + DB_NAME):
    #     with app.app_context():
    #         db.create_all()
    #         print('Database created Successfully')

    return app