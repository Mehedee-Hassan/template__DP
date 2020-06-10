
"""
Created on Tue Jun  9 14:15:06 2020

@author: mehedee
"""

import json
import pandas as pd


class Config:
    
    _file = 'C:\\Users\\mehedee\\Documents\\data\\weatherdata\\miyazaki_shi\\weater_data_miyazaki_shi_2016-1.csv'
    _csvTitle = "date,hour,temperature,rainfall"
    
    def getConfig (self):
        return { "file" : self._file,'csv_title':self._csvTitle }
    





config = (Config()).getConfig()
data = pd.read_csv(config['file'])
df = pd.DataFrame(data)
                
df.sort_values(["date",'hour'], axis = 0, ascending = True,inplace = True, na_position ='last') 




# make flat
