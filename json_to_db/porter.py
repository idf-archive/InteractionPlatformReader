# -*- coding: UTF-8 -*-
import codecs
from settings import *
import  json
import os
from json_to_db.models.models import *

__author__ = 'Danyang'

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
                    stock_type = item["stocktype"]
                    stock = Stock(stock_code=stock_code,
                                  stock_type=stock_type
                                  )
                    stock.save()
                    # parsing Speculator
                    is_guest = bool(item["q_isguest"])
                    name = item["q_name"]
                    speculator = Speculator(name=name,
                                            is_guest=is_guest
                                            )
                    speculator.save()
                    # parsing Question
                    id = item["q_id"]
                    datetime = item["q_date"]
                    content = item["q_content"]
                    q_is_close_comment = bool(item["q_isclosecomment"])
                    c_is_close_comment = bool(item["c_isclosecomment"])
                    q_is_close_appraise = bool(item["q_iscloseappraise"])
                    c_is_close_appraise = bool(item["c_iscloseappraise"])
                    is_canceled = bool(item["hasCancel"])
                    score = item["score"]
                    stock_code = stock
                    speculator_name = speculator
                    question = Question(id=id,
                                        datetime=datetime,
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
                    question.save()
                    item_list = [stock, speculator, question]
                    if "reply" in item:
                        for reply in item["reply"]:
                            # parsing Management
                            name = reply["r_name"]
                            office_name = reply["r_officename"]
                            stock_code = stock
                            management = Management(name=name,
                                                    office_name=office_name,
                                                    stock_code=stock_code)
                            management.save()
                            # parsing Reply
                            id = reply["r_content"]
                            datetime = reply["r_date"]
                            content = reply["r_content"]
                            is_check = bool(reply["isCheck"])
                            question_id = question
                            management_param = management
                            reply = Reply(id=id,
                                          datetime=datetime,
                                          content=content,
                                          is_check=is_check,
                                          question_id = question_id,
                                          management=management_param,
                                          )
                            reply.save()

                            item_list.append(management)
                            item_list.append(reply)




                    break
            break # testing






