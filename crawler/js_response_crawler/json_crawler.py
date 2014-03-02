

__author__ = 'Danyang'
import codecs
import json
import requests
import time

# r_id=0, 2k+ pages
# for r_id \in [1, 2656) no topics
class IrcsCrawler(object):
    def __init__(self, r_id):
        self.pageNo = 1
        self.r_id = r_id

    def __parse(self):
        while True:
            # request
            try:
                payload = {'pageNo': self.pageNo, 'rid': self.r_id}
                r = requests.post('http://ircs.p5w.net/ircs/topicInteraction/questionPage.do', data=payload)
                r_dict = json.loads(r.text)
            except requests.ConnectionError as e:
                print e.message
                time.sleep(5)
                continue

            # parse
            status = r_dict["status"]

            try:
                value = json.loads(r_dict["value"])
            except ValueError as e:
                print e.message
                break

            if status!="Y":
                break

            page_count = value["pagecount"]
            print "crawling topic %d, page %d/%d" % (self.r_id, self.pageNo, page_count)
            if page_count<=0:
                break


            # writing
            qna_list = value["q_all"]
            stock_code = qna_list[0]["stockcode"]
            qna_json = json.dumps(qna_list, ensure_ascii=False, encoding='utf-8')
            self.__write_to_file(qna_json, stock_code)

            # next page
            self.pageNo += 1
            if self.pageNo>page_count:
                break




    def __write_to_file(self, string, stock_code):
        # file IO
        filename = "json_raw/%s-%d-%d.%s" % (stock_code, self.r_id, self.pageNo, "json")
        with codecs.open(filename, "w", encoding="utf-8") as f:
            f.write(string)

    def do_job(self):
        self.__parse()


