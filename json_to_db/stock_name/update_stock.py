# -*- coding: UTF-8 -*-
import codecs
import os
from peewee import  *
__author__ = 'Danyang'
from json_to_db.models.models import Stock
def update_stock():
    path = os.path.dirname(__file__).replace("\\", "/")+'\stock.txt'
    with codecs.open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            lst = line.split()
            stock_code = lst[0]
            stock_name = lst[1]
            try:
                stock = Stock.get(Stock.stock_code==stock_code)
                stock.company_name = stock_name
                stock.save()

            except DoesNotExist:
                pass