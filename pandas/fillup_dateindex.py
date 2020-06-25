import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
from statsmodels.tsa.ar_model import AR, ARResults

data_path = 'C:\\Users\\mehedee\\Documents\\data\\'
file = 'xx.csv'

df = pd.read_csv(data_path+file,index_col='date',parse_dates=True)


idx = pd.date_range(str(df.index[0]), str(df.index[-1]))

s = df
s.index = pd.DatetimeIndex(s.index)

s = s.reindex(idx, fill_value=0)
print(s)



# how much dates were null
count = 0
for index,row in df.iterrows():
    if row['count'] == 0:
        print(row)
        count += 1
        
print('COUNT = ',count)
  