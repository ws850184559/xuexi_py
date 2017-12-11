# encoding:UTF-8
import pymysql      # python 数据库操作库
import os  
import time
import sys
import re   # 网络请求库

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', charset= "utf8", use_unicode = False)    # 连接服务器
cur = conn.cursor()     # 连接数据库
sectionsql = "SELECT * FROM xue_baozou.sectionBook WHERE sectionParentsign = 'vXS6F5A9Klz0eIxZhiCCKzvb4WsTz61k'"    # 查询数据库
# print sectionsql # 输出查询语句
cur.execute(sectionsql) # 执行查询语句
rows = cur.fetchall()   # 得到查询结果

wsstr = ''  # 声明一个字符串
for row in rows:
    wsstr = wsstr + '\n' + row[4] + '\n' + row[3]   # 拼装字符串
# print wsstr
f=open('ws0911a.txt', 'a')  # 写入本地当前文件夹 名字为 ws0911a.txt 
# file object = open(file_name [, access_mode][, buffering])
#  各个参数的细节如下：

#     file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
#     access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
#     buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
# 不同模式打开文件的完全列表：
# 模式	描述
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

# 字符串替换
strinfo = re.compile('<br/>')
b = strinfo.sub('', wsstr)
strinfo2 = re.compile('&#13')
c = strinfo2.sub('', b)
f.write(c)  # 执行写入语句
f.close()   # 关闭写入
