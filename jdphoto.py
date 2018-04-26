#!/usr/bin/env python
# coding=utf-8
import re
import urllib.request
def craw(url,page):
    html = urllib.request.urlopen(url).read().decode("utf-8")
    html = str(html)
    pat1=' <img width="220" height="220" data-img="1".+?>'
    result1 = re.compile(pat1).findall(html)
    for i in range(0,len(result1)):
        print("开始爬取第"+str(page)+"页第"+str(i)+"图片......")
        result = result1[i]
        pat2 = '//(.+?\.com.+?\.\w\wg)'
        #pat2 = '//(.+?\.[jp][pn]g)'
        image = re.compile(pat2).findall(result)
        image = image[0]
        imagename = "./photo/" + str(page) + "-" + str(i) + ".jpg"
        imageurl = "http://" + image
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(i,e.code)
            if hasattr(e,"reason"):
                print(i,e.reason)
def main():
    pages = int(input("print input the number of pages what you want to get:"))
    for i in range(1,pages+1):
        url = "https://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
        craw(url,i)
#craw("https://list.jd.com/list.html?cat=9987,653,655&page=2",2)
main()
