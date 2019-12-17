#!/usr/bin/env python
# coding:utf-8



# import re
# pattern = re.compile(ur'<time datetime="2019-11-28 5:19:41">2019-11-28 5:19:41</time>')
# str = u'1988-05-20'
# print(pattern.search(str))


import re
pattern = re.compile('\d{4}(\-|\/|.)\d{1,2}\1\d{1,2}')
str = ' 2019-11-28 5:19:41</time> '
str1 = '<time datetime="2019-11-28 5:19:41">2019-11-28 5:19:41</time>'
res =  r'([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))'

li = re.findall(res,str1)
print(li)
result = re.match(pattern, str)
print(pattern.search(str))
print("1"==1)


