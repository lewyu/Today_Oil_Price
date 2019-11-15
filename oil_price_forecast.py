from __future__ import print_function
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.setrecursionlimit(99999)
import time
from progressbar import *

total = 1000

def dosomework():
    time.sleep(0.01)

progress = ProgressBar()

for i in progress(range(1000)):
    dosomework()
'''
载入数据
'''
print("载入数据-------")
data_his = pd.read_excel("src/history.xlsx")  # 历史
data_his.fillna(value=-99999, inplace=True)

data_cur = pd.read_excel("src/current.xlsx")  # 当前
data_cur.fillna(value=-99999, inplace=True)

'''
拆分数据
'''
print("拆分数据-------")
learn_x = np.delete(data_his.values, ['0', '1', '5', '6', ], axis=1)
learn_y = np.delete(data_his.values, ['0', '2', '3', '4', '5', '6'], axis=1)
learn_x = np.delete(learn_x, [0], 0)
learn_y = np.delete(learn_y, [0], 0)

pre_y = np.delete(data_cur.values, ['0', "1", '5', '6'], axis=1)
pre_y = np.delete(pre_y, [0], 0)

'''
载入学习模型
'''
from sklearn import svm

model_SVR = svm.SVR()

'''
学习历史数据
'''
model_SVR.fit(learn_x, learn_y)

'''
预测数据
'''
result = model_SVR.predict(pre_y)

'''
输出结果及绘图
'''
print(result)
plt.figure()
plt.title('Predict Value: ' + str(result))
plt.plot(np.arange(len(result)), result, 'ro-', label='predict value')
plt.legend()
plt.show()