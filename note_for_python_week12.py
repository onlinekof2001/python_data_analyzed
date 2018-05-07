# -*- coding: utf-8 -*-
from __future__ import division
from pandas import Series,DataFrame
from numpy.random import randn
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import timedelta
plt.rc('figure',figsize=(12, 4))
pd.options.display.max_rows = 12
np.set_printoptions(precision=4, suppress=True)

current = datetime.now()
print current

SCN=datetime.now() - datetime(1970, 01, 01)
print SCN,SCN.days,SCN.seconds

beginning = datetime.now()
print beginning + timedelta(12) 

datestrs = ['7/6/2012','5/1/2016']
print [datetime.strptime(x, '%m/%d/%Y') for x in datestrs]


dates = [datetime(2016,4,11),datetime(2016,4,15),datetime(2016,4,18),datetime(2016,4,19)]
ts = Series(np.random.randn(4),index=dates)
print ts
ts.shift(1,freq='M')

ts1 = pd.date_range('1/1/2018','12/1/2018',freq='BM')
pd.date_range('1/1/2018','1/3/2018',freq='90T')
print ts1

from pandas.tseries.offsets import Day,MonthEnd

now = datetime.now()
now + 3 * Day()

now + MonthEnd(2)

offset = MonthEnd()
offset.rollforward(now)
offset.rollback(now)

path = u'D:\Software\第12周\stock_px.csv'
data = pd.read_csv(path,parse_dates=True, index_col=0)


data_value = data[['AAPL','MSFT','XOM','SPX']]
data_value = pd.DataFrame(data_value,dtype=np.float64)
'''data_value = data_value.resample('B').ffill()'''
data_value.info
plt.rcParams['axes.unicode_minus'] = False
for d in data_value['AAPL'],data_value['MSFT'],data_value['XOM'],data_value['SPX']:
 d.plot()
 plt.legend(loc='best')
 plt.show()

forecastnum = 5

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
for dv in data_value['MSFT'],data_value['XOM'],data_value['SPX']:
    plot_acf(dv).show()
    plt.title(dv.name)


from statsmodels.tsa.stattools import adfuller as ADF
for adv in data_value['MSFT'],data_value['XOM'],data_value['SPX']:
    print(ADF(adv), adv.name)

plt.subplot(1,3,1)
dvm = data_value['MSFT'].diff().dropna()
plt.title(dvm.name)  
dvm.plot()
plt.subplot(1,3,2)
dvx = data_value['XOM'].diff().dropna()
plt.title(dvx.name)
dvx.plot()  
plt.subplot(1,3,3)
dvs = data_value['SPX'].diff().dropna()
plt.title(dvs.name)
dvs.plot() 

  
for i in dvm,dvx,dvs:
    plot_acf(i).show()
    plt.title(i.name)


from statsmodels.stats.diagnostic import acorr_ljungbox
for bdv in dvm,dvx,dvs:
    print acorr_ljungbox(bdv, lags=1)


from statsmodels.tsa.arima_model import ARIMA
pmax = int(len(dvm)/10)
qmax = int(len(dvm)/10)
bic_matrix = []
for p in range(pmax + 1):
    tmp=[]
    for q in range(qmax + 1):
        try:
            tmp.append(ARIMA(data_value['MSFT'],(p,1,q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)print model.summary2
    
bic_matrix = pd.DataFrame(bic_matrix)
p,q = bic_matrix.stack().idxmin()
print(u'BIC minimum P value & Q value is: %s, %s' %(p,q))
model_MSFT= ARIMA(dvm,(0,1,1)).fit()
model_XOM = ARIMA(dvm,(0,1,1)).fit()
model_SPX = ARIMA(dvm,(0,1,1)).fit()
