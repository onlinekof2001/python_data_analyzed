import numpy as np
import pandas as pd
from pandas import Series,DataFrame

data = pd.read_csv('D:/Software/week8/data/tips.csv', float_format = '%.3f%')
tipbytime = data['tip'].groupby(data['time'])
tipbytime.mean()
tipbytime.var()

tbillbysex = data.groupby('sex')['total_bill']
tipbysex = data['tip'].groupby(data['sex'])
tbillbysex.mean()
tbillbysex.std()

for i in data.index:
    if data.loc[i]['sex'] == 'Female':
        print (i,(data.loc[i]['total_bill'] - tbillbysex.mean()[0])/tbillbysex.std()[0],
        (data.loc[i]['tip'] - tbillbysex.mean()[0])/tbillbysex.std()[0])
    else:
        print (i,(data.loc[i]['total_bill'] - tbillbysex.mean()[1])/tbillbysex.std()[1],
        (data.loc[i]['tip'] - tbillbysex.mean()[1])/tbillbysex.std()[1])
        
tipbysmoker = data.groupby('smoker')['tip']

tipbysmoker.mean()[0]
tipbysmoker.sum()
round(data['tip'].sum(),2)

data['tip_pct'] = data['tip'] / data['total_bill']

data.groupby('smoker')['tip_pct'].mean()