
import re
import time
import urllib
# from collections import OrderedDict
# from bs4 import BeautifulSoup  
import pymysql
import requests
# import HTMLParser
# import random
from pyquery import PyQuery as pq
# book 表的SQL
# CREATE TABLE `xue_baozou`.`book`  (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `bookname` char(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
#   `bookAuthor` char(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
#   `time` char(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
#   `bookurl` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
#   `booksign` char(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
#   PRIMARY KEY (`id`) USING BTREE,
#   INDEX `book_ibfk_1`(`booksign`) USING BTREE
# ) ENGINE = InnoDB AUTO_INCREMENT = 10851 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

#sectionBook SQL
# CREATE TABLE `xue_baozou`.`sectionBook`  (
#   `sectionID` int(11) NOT NULL AUTO_INCREMENT,
#   `sectionParentsign` char(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
#   `sectionURL` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
#   `sectionContent` text CHARACTER SET utf8 COLLATE utf8_general_ci,
#   `sectionname` char(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
#   `sections` char(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
#   PRIMARY KEY (`sectionID`) USING BTREE,
#   INDEX `sectionParentsign`(`sectionParentsign`) USING BTREE,
#   INDEX `sectionParentsign_2`(`sectionParentsign`) USING BTREE,
#   INDEX `sectionParentsign_3`(`sectionParentsign`) USING BTREE,
#   INDEX `sectionParentsign_4`(`sectionParentsign`) USING BTREE
# ) ENGINE = InnoDB AUTO_INCREMENT = 25381 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


def getTextList(wsurl, wsbooknames, wszuozhes, wsshijians):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    salt = ''
    for i in range(32):
        sa.append(random.choice(seed))
        salt = ''.join(sa)
    booksign = salt
    print salt
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', charset="utf8",use_unicode = False)    #连接服务器
    cur = conn.cursor()
    booksql = "insert into xue_baozou.book(bookname,bookAuthor,time,bookurl,booksign) values(%s,%s,%s,%s,%s)"
    param = (wsbooknames.encode('utf-8'), wszuozhes.encode('utf-8'), wsshijians, wsurl, booksign.encode('utf-8'))
    try:
        A = cur.execute(booksql, param)
        conn.commit()
    except Exception as identifier:
        print(identifier)
        conn.rollback()
        return

    wsre = requests.get(wsurl)
    doc = pq(wsre.text)

    listss = pq(doc('dd'))
    wsqi=0
    for wsdd in listss:
        if wsqi > 8:
            print wsqi
            print pq(pq(wsdd)('a')).attr('href')
            wsbookurl = pq(pq(wsdd)('a')).attr('href')
            time.sleep(0.5)
            wsbookre = requests.get(wsbookurl)
            wsbookdoc = pq(wsbookre.text)
            wsbookcontent = wsbookdoc('div').filter('#content').html()
            # print wsbookdoc('div').filter('#content').html()
            wsbooksectionname = wsbookdoc('h1').text()
            sections = wsqi-8
            print wsbookname
            sql = "insert into xue_baozou.sectionBook(sectionParentsign,sectionURL,sectionContent,sectionname,sections) values(%s,%s,%s,%s,%s)"
            param = (booksign.encode('utf-8'), wsbookurl.encode('utf-8'), wsbookcontent.encode('utf-8'), wsbooksectionname.encode('utf-8'),sections)
            try:
                A = cur.execute(sql, param)
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
        wsqi = wsqi+1

# url = 'http://www.biquge5200.com/modules/article/search.php?searchkey=盗墓笔记’
url ='http://www.biquge5200.com/modules/article/search.php?searchkey=%E7%9B%97%E5%A2%93%E7%AC%94%E8%AE%B0'
url = 'http://www.biquge5200.com/modules/article/search.php?searchkey=%E8%BF%91%E8%BA%AB%E5%85%B5%E7%8E%8B'
headers = {
    'User-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Host' : 'm.weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding' : 'gzip, deflate, br',
    # 'Referer' : 'https://m.weibo.cn/status/' + weibo_id,
    'Cookie' : '_T_WM=e25a28bec35b27c72d37ae2104433873; WEIBOCN_WM=3349; H5_wentry=H5; backURL=http%3A%2F%2Fm.weibo.cn%2F; SUB=_2A250zXayDeThGeVJ7VYV8SnJyTuIHXVUThr6rDV6PUJbkdBeLRDzkW1FrGCo75fsx_qRR822fcI2HoErRQ..; SUHB=0sqRDiYRHXFJdM; SCF=Ag4UgBbd7u4DMdyvdAjGRMgi7lfo6vB4Or8nQI4-9HQ4cLYm_RgdaeTdAH_68X4EbewMK-X4JMj5IQeuQUymxxc.; SSOLoginState=1506346722; M_WEIBOCN_PARAMS=featurecode%3D20000320%26oid%3D3638527344076162%26luicode%3D10000011%26lfid%3D1076031239246050; H5_INDEX=3; H5_INDEX_TITLE=%E8%8A%82cao%E9%85%B1',
    'DNT' : '1',
    'Connection' : 'keep-alive',
    }
i = 0
while True:
    response = requests.get(url=url)
    doc = pq(response.text)
    if i == 0 :
        qq = 0
        li = doc('tr')
        for s in li :
            ws = pq(s).text()
            ws2 = pq(pq(s)('tr'))
            ws3 = pq(pq(ws2)('td'))
            wsi = 0
            wsbookname = ''
            wszuozhe = ''
            wsshijian = ''
            haveurl = ''
            for td in ws3:
                
                if pq(td).filter('.odd'):
                    if pq(pq(td)('a')).html() != None:
                        wsbookname = pq(pq(td)('a')).html()
                        # print wsbookname #名字
                        haveurl = pq(pq(td)('a')).attr('href')  # 书的url的地址
                    else:
                        
                        if wsi == 0 :
                            wszuozhe = pq(td).html()
                            # print ('作者-'+wszuozhe.encode('utf-8'))
                            wsi = wsi + 1
                        else:
                            wsshijian = pq(td).html()
                            # print ('时间-'+wsshijian.encode('utf-8'))
                        pass
                    
                    pass
                    
                      
            print('书名-'+wsbookname.encode('utf-8') + '   作者-' + wszuozhe.encode('utf-8')+'  时间' + wsshijian.encode('utf-8'))  
            if wsbookname != '': 
                getTextList(haveurl, wsbookname, wszuozhe, wsshijian)

    i = i+1


