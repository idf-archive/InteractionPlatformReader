###Required Package
```shell
$pip install -r requirements.txt
```
###General Adminstration Information
####Server
Server running as @NBSRESEARCHSVR.
####The nature of the raw data, the source of the data, and the time period.
Nature - 公司业绩说明会, 公司高层与网民的交流信息  
File Format - [json](http://en.wikipedia.org/wiki/JSON) and in the MySql database  
Source - http://ircs.p5w.net/  
Time period - Crawled at 2 March 2014. Data from 2009 to 2013.  
####The program codes used to crawl the data and where the raw data are stored on the server.
Crawler code: `/data/danyang/projects/qna/src/crawler/js_response_crawler`  
Data craled: `/data/danyang/projects/qna/data`  
To run the code: 
```shell
$ cd /data/danyang/projects/qna/src/crawler/js_response_crawler
$ python main.py
``` 
####The program codes used to create the final database and indicate where to find the database.
Database Data Import code: `/data/danyang/projects/qna/src/json_to_db`  
To run the code:
```shell
$ cd /data/danyang/projects/qna/src
$ python shell.py
```
Locate the database:
```shell
$ mysql -u website -p
mysql> use qna;
mysql> SELECT * FROM STOCK LIMIT 20;
```