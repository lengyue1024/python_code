#!/bin/bash/python
#coding=utf-8

# 导入模块
import prettytable as pt
import requests
from bs4 import BeautifulSoup
url = "http://news.qq.com/"
# 请求腾讯新闻的ＵＲＬ
data = requests.get(url).text
# 对请求的页面进行解析
soup = BeautifulSoup(data,'lxml')
# 从解析文件中通过select选择器定位到指定的元素，并返回一个列表
news_titles = soup.select("div.text > em.f14 > a.linkto")
# 设置表格标题栏
tb = pt.PrettyTable(["标题","链接"])
# 对返回的列表进行遍历
for n in news_titles:
	# 提取出标题和链接信息
	title = n.get_text()
	link = n.get("href")
	tb.add_row([title,link])
# 以表格形式打印
print(tb)
