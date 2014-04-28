__author__ = 'Danyang'
from models import *
from peewee import *
def create_table():
    database.connect()
    table_lst = [Stock, Speculator, Management, Question, Reply]
    for item in table_lst:
        try:
            item.drop_table()
        except OperationalError:
            pass

    for item in table_lst:
        item.create_table()


if __name__=="__main__":
    create_table()




