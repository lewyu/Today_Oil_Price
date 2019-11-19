import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 500)
dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off

fig, ax = plt.subplots()
line1, = ax.plot(x, np.sin(x), '--', linewidth=2,
                 label='Dashes set retroactively')
line1.set_dashes(dashes)

line2, = ax.plot(x, -1 * np.sin(x), dashes=[30, 5, 10, 5],
                 label='Dashes set proactively')

ax.legend(loc='lower right')
plt.show()


# 读取Excel文件
from xlrd import open_workbook
x_data1=[]
y_data1=[]
wb = open_workbook('src/history.xlsx')
for s in wb.sheets():
    print('Sheet:', s.name)
    for row in range(s.nrows):
        print('the row is:', row)
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(values)
        x_data1.append(values[0])
        y_data1.append(values[1])