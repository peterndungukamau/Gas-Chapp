from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES




bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.login_view = 'vendor.login'
    
    
    
    # configure UploadSet
    configure_uploads(app,photos)
    
    # register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
    
    from .vendor import vendor as vendor_blueprint
    app.register_blueprint(vendor_blueprint,url_prefix='/vendor')
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app