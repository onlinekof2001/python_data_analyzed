# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

my_data=[['slashdot','USA','yes',18,'None'],
['google','France','yes',23,'Premium'],
['digg','USA','yes',24,'Basic'],
['kiwitobes','France','yes',23,'Basic'],
['google','UK','no',21,'Premium'],
['(direct)','New Zealand','no',12,'None'],
['(direct)','UK','no',21,'Basic'],
['google','USA','no',24,'Premium'],
['slashdot','France','yes',19,'None'],
['digg','USA','no',18,'None'],
['google','UK','no',18,'None'],
['kiwitobes','UK','no',19,'None'],
['digg','New Zealand','yes',12,'Basic'],
['slashdot','UK','no',21,'None'],
['google','UK','yes',18,'Basic'],
['kiwitobes','France','yes',19,'Basic']]

my_data=DataFrame(my_data)
my_data.columns=['site', 'country', 'boolen', 'year', 'type']
x=my_data.iloc[:,:4].as_matrix()
y=my_data.iloc[:,:4].as_matrix()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

clf = KNeighborsClassifier(algorithm='kd_tree')
clf.fit(x_train, y_train)

answer = clf.predict(x_test)
print 'KNN-Precision:%s' %(np.mean( answer == y_test))

#贝叶斯分类器
clf = BernoulliNB()
clf.fit(x_train,y_train)

answer = clf.predict(x_test)
print'Bayes-Precision:%s'%(np.mean( answer == y_test))


#决策树模型
from sklearn.tree import DecisionTreeClassifier as DTC
dtc = DTC(criterion='entropy') #建立决策树模型，基于信息熵
dtc.fit(x_train, y_train) #训练模型
#导入相关函数，可视化决策树。
#导出的结果是一个dot文件，需要安装Graphviz才能将它转换为pdf或png等格式。
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open("tree.dot", 'w') as f:
  f = export_graphviz(dtc, out_file = f)

answer = dtc.predict(x_test)
print 'DecisionTree-Precision:%s' %(np.mean( answer == y_test))

#SVM模型
from sklearn.svm import SVC
clf =SVC()
clf.fit(x_train, y_train)

answer = clf.predict(x_test)

print 'SVM-Precision:',(np.mean( answer == y_test))
