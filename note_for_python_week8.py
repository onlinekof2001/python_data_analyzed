import numpy as np
import pandas as pd
from pandas import Series,DataFrame

data = pd.read_csv('D:/Software/week8/data/tips.csv')
tipbytime = data['tip'].groupby(data['time'])
tipbytime.mean()
tipbytime.var()

tbillbysex = data['total_bill'].groupby()