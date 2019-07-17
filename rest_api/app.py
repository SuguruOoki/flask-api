from flask import Flask

from rest_api import settings
from rest_api.apis import api
from rest_api.models import db

# Flask本体
app = Flask(__name__)


def configure_app(flask_app: Flask) -> None:
    # DB接続先情報やSwaggerの表示形式を指定
    flask_app.config['SQLALCHEMY_DATABASE_URI']        = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION']       = settings.SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE']              = settings.RESTPLUS_VALIDATE


def initialize_app(flask_app: Flask) -> None:
    # FlaskへAPIやDB情報を登録
    configure_app(flask_app)
    api.init_app(flask_app)
    db.init_app(flask_app)
    db.create_all(app=flask_app)


def main() -> None:
    # Flaskを初期化して実行
    initialize_app(app)
    app.run(host='0.0.0.0', debug=settings.DEBUG)


if __name__ == '__main__':
    main()
