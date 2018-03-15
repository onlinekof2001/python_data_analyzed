import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

data = pd.read_csv('D:/Software/week8/data/tips.csv')
tipbytime = data['tip'].groupby(data['time'])
tipbytime.agg(['mean','var'])

tbillbysex = data.groupby('sex')['total_bill']
tipbysex = data['tip'].groupby(data['sex'])
tbillbysex.mean()
tbillbysex.std()


def standard(val):
    return (val - val.mean())/val.std()
    
data.groupby('sex')[['total_bill','tip']].apply(standard).join(data['sex'])

for i in data.index:
    if data.loc[i]['sex'] == 'Female':
        print (i,(data.loc[i]['total_bill'] - tbillbysex.mean()[0])/tbillbysex.std()[0],
        (data.loc[i]['tip'] - tbillbysex.mean()[0])/tbillbysex.std()[0])
    else:
        print (i,(data.loc[i]['total_bill'] - tbillbysex.mean()[1])/tbillbysex.std()[1],
        (data.loc[i]['tip'] - tbillbysex.mean()[1])/tbillbysex.std()[1])
        
tipbysmoker = data.groupby('smoker')['tip']

tipbysmoker.mean()[0]
tipbysmoker.sum()),2)

data['tip_pct'] = data['tip'] / data['total_bill']
smkavg=data.groupby('smoker')['tip_pct'].mean()
round((smkavg[0] - smkavg[1]),4)
        
def stdrd(val):
    return val.mean(), val.std()
    
data.groupby(['sex','size'])['tip_pct'].apply(stdrd)

data.groupby(['sex','size'])['tip_pct'].agg(['mean','std'])
round(data['tip'].sum(

def ts(val):
    return val.values
tbillbyts = data.groupby(['time','size'])['total_bill'].apply(ts)

xlim(8,8)
ylim(8,8)
for i in np.arange(tbillbyts.count()):
    if len(tbillbyts.values[i]) != 1:
        j = i + 1
        plt.subplot(3,4,j)
        plt.pie(tbillbyts.values[i], autopct='%1.1f%%')
    