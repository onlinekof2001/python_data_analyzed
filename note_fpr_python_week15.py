#-*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

"""
data = load_iris()
y = data.target
X = data.data
pca = PCA(n_components=2)
reduce_X = pca.fit_transform(X)

red_x, red_y = [],[]
blue_x, blue_y = [],[]
green_x, green_y = [],[]
for i in range(len(reduce_X)):
    if y[i] == 0:
        red_x.append(reduce_X[i][0])
        red_y.append(reduce_X[i][1])
    elif y[i] == 1:
        blue_x.append(reduce_X[i][0])
        blue_y.append(reduce_X[i][1])
    else:
        green_x.append(reduce_X[i][0])
        green_y.append(reduce_X[i][1])

plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.show()
"""

os.chdir(u'D:/Software/第15周/')
data = pd.read_csv('ex15.txt',parse_dates=True)
data = pd.DataFrame(data)

X = data.iloc[:,0:3]
y = data.iloc[:,:4]
pca = PCA(n_components=1)
reduce_X = pca.fit_transform(X)

reduce_X


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
linreg = LinearRegression()
linreg.fit(X_train, y_train)

print(linreg.intercept_)
print(linreg.coef_)
print(zip(['x1', 'x2', 'x3'], linreg.coef_))


print "MAE:",metrics.mean_absolute_error(y_test,y_pred)

print "MSE:",metrics.mean_squared_error(y_test,y_pred)

print "RMSE:",np.sqrt(metrics.mean_squared_error(y_test,y_pred))