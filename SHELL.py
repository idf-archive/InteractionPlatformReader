__author__ = 'Danyang'
# execute from python console
from json_to_db.models.mgt import *
from json_to_db.porter import *
from json_to_db.stock_name.update_stock import *

database.connect()
# create_table()
# store_json()
update_stock()