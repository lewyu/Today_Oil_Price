#!/usr/bin/env python
# coding:utf-8
import codecs
import csv

import requests
from pyquery import PyQuery as pq
# 引入excel模块
import openpyxl

def get_page(url):
    """发起请求 获得源码"""
    r = requests.get(url)
    r.encoding = 'GBK'
    html = r.text
    return html

def parse(text, filepath):
    """解析数据 写入文件"""
    doc = pq(text)
    # 获取时间,并写入时间
    times = doc('time')
    with codecs.open(filepath, 'a', 'utf_8_sig') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow([times])
    print(times)
    # 获取表格 # 获得每一行的tr标签
    tds = doc('table  tr').items()

    for td in tds:  # 地区	92号汽油	95号汽油	98号汽油	0号柴油
        place = td.find('td:first-child').text()  # 地区
        oil92 = td.find('td:nth-child(2)').text()  # 92号汽油
        oil95 = td.find('td:nth-child(3)').text()  # 95号汽油
        oil98 = td.find('td:nth-child(4)').text()  # 98号汽油
        oil00 = td.find('td:nth-child(5)').text()  # 0号汽油

        with codecs.open(filepath, 'a', 'utf_8_sig') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow([place, oil92, oil95, oil98, oil00])

    print("文件写入完成！")

if __name__ == "__main__":
    url = "http://oil.usd-cny.com/"
    filepath = 'src/today_oil_price.csv'
    text = get_page(url)
    # print(text)
    parse(text, filepath)
