from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Product import CreateItem, GetAllItem
from Variant import CreateVariant, GetAllVariant

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(CreateItem, '/CreateItem')
api.add_resource(GetAllItem, '/getItem')
api.add_resource(CreateVariant, '/CreateVariant')
api.add_resource(GetAllVariant, '/getVariant')

if __name__ == '__main__':
    app.run(debug=True)
