from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import Column, MetaData, inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from DBOperations import DBOperations
import Constants

app = Flask(__name__)
api = Api(app)


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


class CreateItem(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str)
            parser.add_argument('brand', type=str)
            parser.add_argument('category', type=str)
            parser.add_argument('product_code', type=str)
            args = parser.parse_args()
            engine = create_engine('mysql+pymysql://root:my-secret-pw@192.168.99.100:32785/paytm_inventory_db')
            meta = MetaData(engine)
            table = Table(Constants.Constants.PRODUCT_TABLE, meta,
                          Column('product_id', Integer, primary_key=True, autoincrement=True, nullable=False),
                          Column('name', String(45)),
                          Column('brand', String(45)),
                          Column('category', String(45)),
                          Column('product_code', String(45))
                          )
            meta.create_all()

            # insert data via insert() construct
            ins = table.insert().values(
                name=args['name'],
                brand=args['brand'],
                category=args['category'],
                product_code=args['product_code']
            )
            conn = engine.connect()
            conn.execute(ins)

            return {'status': 'Product Entered Successfully'}

        except Exception as e:
            return {'error': str(e)}


class GetAllItem(Resource):
    def get(self):
        try:
            args = request.args
            data_list = DBOperations.get_item_list(args)
            return {'status': 'Product Gathered Successfully', 'data': data_list}

        except Exception as e:
            return {'error': str(e)}


api.add_resource(CreateItem, '/CreateItem')
api.add_resource(GetAllItem, '/getItem')

if __name__ == '__main__':
    app.run(debug=True)
