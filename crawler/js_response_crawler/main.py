from json_crawler import IrcsCrawler
def main():
    # r_id = 8659
    for r_id in range(2089, 3000):
        crawler = IrcsCrawler(r_id)
        crawler.do_job()

if __name__=="__main__":
    main()
