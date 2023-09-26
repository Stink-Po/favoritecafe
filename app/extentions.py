from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail





db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()
ckeditor = CKEditor()
user_login_manager = LoginManager()
user_login_manager.login_view = 'user_login'
migrate = Migrate()





