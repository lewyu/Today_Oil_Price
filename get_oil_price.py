#!/usr/bin/env python
# coding:utf-8
import codecs
import csv

import requests
from pyquery import PyQuery as pq
# 引入excel模块
import openpyxl
# 引入正则表达式
import re


def get_page(url):
    """发起请求 获得源码"""
    r = requests.get(url)
    r.encoding = 'GBK'
    html = r.text
    return html


def parse(text, filepath):
    """解析数据 写入文件"""
    doc = pq(text)
    # 获取时间,并写入times
    times = doc('time')

    # 正则化时间
    res = '(?<=").*?(?=")'  # 取双引号内容
    times = str(times)  # 转string类型
    li = re.findall(res, times)  # 正则部分
    li = str(li)  # 转string类型
    times = li[2:12]  # 取标准日期格式

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


# def read_excel_xlsx(path, sheet_name):
#     workbook = openpyxl.load_workbook(path)
#     # sheet = wb.get_sheet_by_name(sheet_name)这种方式已经弃用，不建议使用
#     sheet = workbook[sheet_name]
#     for row in sheet.rows:
#         for cell in row:
#             print(cell.value, "\t", end="")
#         print()


if __name__ == "__main__":
    url = "http://oil.usd-cny.com/"
    filepath = 'src/today_oil_price.csv'
    # sheet_name = 'today_oil_price'
    text = get_page(url)
    # print(text)
    parse(text, filepath)
    # read_excel_xlsx(filepath, sheet_name)
