from sqlalchemy import create_engine, MetaData, select
from Helpers import Helpers
from Constants import Constants


class DBOperations:
    db_url = 'mysql+pymysql://root:my-secret-pw@192.168.99.100:32785/paytm_inventory_db'

    @staticmethod
    def get_db_engine():
        return create_engine(DBOperations.db_url)

    @staticmethod
    def get_meta():
        return MetaData(DBOperations.get_db_engine(), reflect=True)

    @staticmethod
    def get_item_list(qp):
        table = DBOperations.get_meta().tables[Constants.PRODUCT_TABLE]
        select_st = select([table])
        conn = DBOperations.get_db_engine().connect()
        if 'item_id' in qp:
            select_st = select([table]).where(table.c.product_id == qp['item_id'])

        res = conn.execute(select_st)
        data_list = Helpers.generate_list(res)
        return data_list
