from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_migrate import Migrate
import os
from app.config import config, cache_config, redis_connection

db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
r_connection = None

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    print(f"app_context: {app_context}")

    app = Flask(__name__)
    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)

    db.init_app(app)
    migrate.init_app(app, db, version_table='alembic_version_inventario')

    cache_configuration = cache_config[app_context if app_context else 'development']
    cache.init_app(app, config=cache_configuration)

    global r_connection
    r_connection = redis_connection[app_context if app_context else 'development']

    from app.resources.resource import inventario
    app.register_blueprint(inventario, url_prefix='/api/v1')

    return app

