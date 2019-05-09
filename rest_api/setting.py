from os import environ

# デバッグモードを有効化
DEBUG = True

# Swaggerのデフォルト表示形式をListにする
SWAGGER_UI_DOC_EXPANSION = 'list'
# Validationの有効化
RESTPLUS_VALIDATE = True

# SQL接続情報
# コンテナ側に環境変数として渡すためこの形式で受け取る
SQLALCHEMY_DATABASE_URI = environ['MYSQL_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = True
