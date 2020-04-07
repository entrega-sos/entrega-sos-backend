import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions
from app import config
from app.config import logger
from app.api.models import db
from app.api.common.errors import handle_error

load_dotenv(find_dotenv())


def create_app():
    logger.info(f'Starting app in {config.ENV_APP} environment')

    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False
    for code in default_exceptions:
        app.register_error_handler(code, handle_error)

    db.init_app(app)

    from app.api.resources.v1 import api_v1
    app.register_blueprint(api_v1, url_prefix='/v1')

    return app


if __name__ == '__main__':
    app.run()