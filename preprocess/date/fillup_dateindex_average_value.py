# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:02:50 2020

@author: mehedee
"""


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error,mean_squared_error

import datetime as dt1
from datetime import datetime as dt2


%matplotlib qt

datapath2 = 'C:\\Users\\mehedee\\Documents\\data\\' 
datafile = 'xxxxxx.csv'


df2 = pd.read_csv(datapath2 + datafile,parse_dates=True)

# parse date column as datetime 
df2['date'] = pd.to_datetime(df2['date'])
# set date column as index column of dataframe

df2 = df2.set_index('date')


# keep df safe if needed for later
df=df2

def seven_days_avg ( data, index, first ,last ,day_up_to):
    
    previous_sum = 0
    # if not equal to -1
    after_sum = 0
    

    count_prev = 0
    count_after = 0
    for i in range(1,day_up_to):
        
#         print("only data",data.iloc[index-i])
        if index - i >= first:        
            tempprev = data.iloc[index-i]['count']
    #             print('prev',tempprev)
            
            if tempprev > 0:
                previous_sum += tempprev
            
                count_prev += 1
            
            
        if index + i < last:        
            tempafter = data.iloc[index+i]['count']
#             print("now" ,tempafter)
            
            if tempafter > 0:
                after_sum += tempafter
    
                count_after += 1
        
        
        
    if after_sum > 0 and previous_sum > 0:
        after_sum = after_sum / count_after
        previous_sum = previous_sum / count_prev

        return ((after_sum+previous_sum)/2)
    elif after_sum > 0:
        after_sum = after_sum / count_after
        return after_sum
    elif previous_sum > 0:
        previous_sum = previous_sum / count_prev
        return previous_sum
    return 0
        

# code porting for fill up date index
# this code is from out side so I had to port this way 
# my code thought ;P
# data to fill the non existent value
fillup_data = -100012349567890001

# porting my codes data as input
data_path =datapath2
file = datafile


# not needed ,just to see all the dates
idx = pd.date_range(str(df2.index[0]), str(df2.index[-1]))

# make a copy to experiment
s = df2
# set index as date
s.index = pd.DatetimeIndex(s.index)

# 1. experiment with average 
s = s.reindex(idx,fill_value=fillup_data)
# print(s)
# 2. experiment with 0
# s = s.reindex(idx, fill_value=-1)

# after fill up date is re-indexed
s = s.reset_index()
s = s.rename(columns={'index': 'date'})


firstpos = 0
lastpos = len(s)

# how much dates were null
count = 0
print('change date entry =')
for index,row in s.iterrows():
    
    
#     check null date existance
#     dateonly = (str(row['date'].year)+'/'+str(row['date'].month)+'/'+str(row['date'].day))
#     if dateonly== '2017/1/1':
    
    
    
    if row['count'] ==fillup_data:
        
        s.loc[index ,'count'] = seven_days_avg(s,index,firstpos,lastpos,8)
        count += 1


# send bak to df my experiment is over
df=s

df.reset_index()
df = df.set_index('date')


df.head()
