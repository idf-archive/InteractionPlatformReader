# -*- coding: UTF-8 -*-
import codecs
import datetime
from settings import *
import  json
import os
from json_to_db.models.models import *

__author__ = 'Danyang'

DATETIME_MASK = "%Y-%m-%d %H:%M:%S.0"
def store_json():
    for root, _, files in os.walk(DATA_PATH):
        for f in files:
            file_path = os.path.join(root, f)
            with codecs.open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                content = json.loads(content)
                for item in content:
                    # parsing Stock
                    stock_code = item["stockcode"]
                    stock_type = item.get("stocktype", "S")
                    try:
                        stock = Stock.get(Stock.stock_code==stock_code)
                    except DoesNotExist:
                        stock = Stock.create(stock_code=stock_code,
                                      stock_type=stock_type
                                      )

                    # parsing Speculator
                    is_guest = bool(item["q_isguest"])
                    name = item["q_name"]
                    try:
                        speculator = Speculator.get(Speculator.name==name)
                    except DoesNotExist:
                        speculator = Speculator.create(name=name,
                                                is_guest=is_guest
                                                )

                    # parsing Question
                    id = item["q_id"]
                    try:
                        timestamp =  datetime.datetime.strptime(item["q_date"], DATETIME_MASK)
                    except ValueError:
                        timestamp = 0
                    content = item["q_content"]
                    q_is_close_comment = bool(item.get("q_isclosecomment", 1))
                    c_is_close_comment = bool(item.get("c_isclosecomment", 1))
                    q_is_close_appraise = bool(item.get("q_iscloseappraise", 1))
                    c_is_close_appraise = bool(item.get("c_iscloseappraise", 1))
                    is_canceled = bool(item["hasCancel"])
                    score = item.get("score", -999)
                    stock_code = stock
                    speculator_name = speculator
                    try:
                        question = Question.get(Question.id==id)
                    except DoesNotExist:
                        question = Question.create(id=id,
                                            datetime=timestamp,
                                            content=content,
                                            q_is_close_comment=q_is_close_comment,
                                            c_is_close_comment=c_is_close_comment,
                                            q_is_close_appraise=q_is_close_appraise,
                                            c_is_close_appraise=c_is_close_appraise,
                                            is_canceled=is_canceled,
                                            score=score,
                                            stock_code=stock_code,
                                            speculator_name=speculator_name,
                                            )

                    item_list = [stock, speculator, question]
                    if "reply" in item:
                        for reply in item["reply"]:
                            # parsing Management
                            name = reply["r_name"]
                            office_name = reply["r_officename"]
                            stock_code = stock
                            try:
                                management = Management.get(Management.office_name==office_name)
                            except DoesNotExist:
                                management = Management.create(name=name,
                                                        office_name=office_name,
                                                        stock_code=stock_code)
                            # parsing Reply
                            id = reply["r_id"]
                            try:
                                timestamp = datetime.datetime.strptime(reply["r_date"], DATETIME_MASK)
                            except ValueError:
                                timestamp = 0

                            content = reply["r_content"]
                            is_check = bool(reply["isCheck"])
                            question_id = question
                            management_param = management
                            try:
                                reply = Reply.get(Reply.id==id)
                            except DoesNotExist:
                                reply = Reply.create(id=id,
                                              datetime=timestamp,
                                              content=content,
                                              is_check=is_check,
                                              question_id = question_id,
                                              management=management_param,
                                              )
                            item_list.append(management)
                            item_list.append(reply)

                    print "saved to db ..."
                    for item in item_list:
                        print item







