from flask_restplus import Api

# API情報を指定して初期化
api = Api(
    title='Test Swagger and Flask API',
    version='1.0',
    description='Swaggerを統合したREST APIのサンプル'
)
