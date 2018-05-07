# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
from sklearn.linear_model import LinearRegression
from sklearn import metrics

fn=u'D:\Software\第11周\data1.txt'
data = pd.read_csv(fn,delimiter='\t',encoding='gb2312');

x = data.iloc[:,:6].as_matrix()
y = data.iloc[:,6].as_matrix()


lr = LR()
lr.fit(x, y)
print(u'逻辑回归模型训练结束。')
print(u'模型的平均正确率为： %s' % lr.score(x, y))

fn1=u'D:\Software\第11周\data2.txt'
data1 = pd.read_csv(fn1,delimiter='\t',encoding='gb2312');

x = pd.DataFrame(data1['X'])
y = pd.DataFrame(data1['Y'])

linreg = LinearRegression()
linreg.fit(x, y)
y_pred = linreg.predict(x)
print('Coefficient: \n', linreg.coef_)
print "MSE:", metrics.mean_squared_error(y, y_pred)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x, y)