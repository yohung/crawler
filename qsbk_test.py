#!/usr/bin/env python
# coding=utf-8
import urllib.request
import re
import time
#from hearder import Headers
def getContent(url,pages):
    #模拟浏览器
    #headers = Headers()
    headers = ("User-Agent","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    userpat = '<h2>\n(.*)?\n</h2>'
    contentpat = '<div class="content">\n<span>\n\n(.*?)\n</span>'
    userlist = re.compile(userpat).findall(data)
    contentlist = re.compile(contentpat,re.S).findall(data)
    for i in userlist:
        a = userlist.index(i)
        b = contentlist[a]
        b = b.replace("<br/>","\n")
        print("第%s页第%s位用户：%s"%(pages,a + 1,i))
        print("内容为：\t%s"%b)
        time.sleep(3)
def main():
    pages = int(input("please input thepages you want to watch:"))
    for i in range(1,pages+1):
        url = "https://www.qiushibaike.com/8hr/page/" + str(i)
        getContent(url,i)
main()
