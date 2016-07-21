import os

import flask
from flasgger.base import Swagger
from flasgger.utils import swag_from
from flask import Flask
from flask.ext.cors.extension import CORS
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "specs": [
        {
            "version": "1.0.0",
            "title": "Game Trade",
            "endpoint": 'v1',
            "route": '/v1',
            "description": "Game Trade APP Example"
        }
    ]
}
Swagger(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})
db = SQLAlchemy(app)


@swag_from('swagger/user.yml')
@app.route('/v1/user', methods=['POST'])
def add_user():
    return flask.request.data


if __name__ == '__main__':
    app.run()
