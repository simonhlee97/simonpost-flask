from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_pagedown import PageDown
from simonpostcom.config import Config
from flask_migrate import Migrate
from flaskext.markdown import Markdown


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
# mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    pagedown = PageDown(app)
    # mail.init_app(app)
    migrate = Migrate(app, db)
    Markdown(app)

    from simonpostcom.users.routes import users
    from simonpostcom.posts.routes import posts
    from simonpostcom.main.routes import main
    from simonpostcom.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    

    return app
