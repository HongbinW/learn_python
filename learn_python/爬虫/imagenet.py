"""
取自https://blog.csdn.net/qq_34739497/article/details/80868535
imagenet由于只允许教育邮箱用，因此只能通过其download，下载url
所需工具：对应目录建立data1文件夹，并在image.txt文件中，存入对应URL即可
"""
import requests
import urllib.request
import time#导入包
import os

file=open("C:\\Users\\user\\Desktop\\image.txt",encoding="utf-8")
for i,line in enumerate(file):
    try:
        print(i)
        if i<472:
            continue
        if os.path.exists("./data1/{}.jpg".format(i)):
            print("file exist")
            continue
        web = urllib.request.urlopen(line)
        time.sleep(0.5)#设置时间间隔为3秒
        data = web.read()
        f = open("./data1/{}.jpg".format(i),"wb")
        f.write(data)
        f.close()
    except:
        continue
"""
--------------------- 
作者：一个追逐自我的程序员 
来源：CSDN 
原文：https://blog.csdn.net/qq_34739497/article/details/80868535?utm_source=copy 
版权声明：本文为博主原创文章，转载请附上博文链接！

"""