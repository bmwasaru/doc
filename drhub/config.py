import os

from flask import Flask
from flask_alembic import Alembic
from flask_sqlalchemy import SQLAlchemy

from drhub.api.discourse import discourse

ROOT = os.path.join(os.path.dirname(__file__), os.pardir)

alembic = Alembic()
db = SQLAlchemy()


def create_app(**config):
    app = Flask(
        __name__,
        static_folder=os.path.join(ROOT, 'static'),
        template_folder=os.path.join(ROOT, 'templates'),
    )

    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql:///drhub' or \
        os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_POOL_SIZE'] = 60
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(discourse)

    configure_db(app)

    return app


def configure_db(app):
    alembic.init_app(app)
    db.init_app(app)
