


"""
Created on Tue Jun  9 14:15:06 2020

@author: mehedee
"""

import json
import pandas as pd


class Config:

    _path="C:\\Users\\mehedee\\Documents\\data\\weatherdata\\miyazaki_shi\\"
    _file = 'C:\\Users\\mehedee\\Documents\\data\\weatherdata\\miyazaki_shi\\xxxx.csv'
    _flatFileName =  'xxxx.csv'
    _csvTitle = "date,hour,temperature,rainfall"
    
    def getConfig (self):
        return { "file" : self._file,'csv_title':self._csvTitle,'flat_file_name':self._flatFileName}
    
class Fields:
    date = 'date'
    hour = 'hour'
    temperature = 'temperature'
    rainfall = 'rainfall'
    _title = 'date,temp0h,temp300h,temp600h,temp900h,temp1200h,temp1500h,temp1800h,temp2100h,rain0h,rain300h,rain600h,rain900h,rain1200h,rain1500h,rain1800h,rain2100h,'
    _key_list = ["date","temp0h","temp300h"
                 ,"temp600h","temp900h","temp1200h"
                 ,"temp1500h","temp1800h","temp2100h"
                 ,"rain0h","rain300h","rain600h"
                 ,"rain900h","rain1200h","rain1500h"
                 ,"rain1800h","rain2100h"]
    #"date,hour,temperature,rainfall"

    def getKeyList(self):
        return self._key_list
    
    def getTitle(self):
        return self._title
    
    def getDocumentation(self):
        return 'This class is to define the fields of csv file. _key_list: each field of the new csv file;_title: fields name in string'


def addToTempList(tempList
                  ,index1=-1,index1Val=-1
                  ,index2=-1,index2val=-1
                  ,index3=-1,index3val=-1
                  ,closeblock=[-1,-1,-1]):
    
    if closeblock[0] == -1: #can add to block 1,index1
        
        tempList[index1] = index1Val                                       # added date field 1 time
       
    if closeblock[1] == -1:                                                #can add to block 2,index2
        tempList[index2] = index2val                                       # added temperatures 1 time
      
    if closeblock[2] == -1:                                                #can add to block 3,index3
        tempList[index3] = index3val                                       # added rainfall  1 time
      
        
    
    
    return tempList


def __main__():
    # get all configurations
    config = Config().getConfig()
    fields = Fields()
    
    # read csv files
    data= pd.read_csv(config['file'])
    df = pd.DataFrame(data)
    
    #get key list of new csv file
    key_list = fields.getKeyList()
    
    # TODO check if list not woring 
    tempDictionary = {   str(key_list[0]):'',str(key_list[1]):'',str(key_list[2]):'',str(key_list[3]):''
                  ,str(key_list[4]):'',str(key_list[5]):'',str(key_list[6]):'',str(key_list[7]):''
                  ,str(key_list[8]):'',str(key_list[9]):'',str(key_list[10]):'',str(key_list[11]):''
                  ,str(key_list[12]):'',str(key_list[13]):'',str(key_list[14]):'',str(key_list[15]):'',
                  str(key_list[16]):''}
    
    tempList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    firstTimeDateAdded = False
    isFirst= False
    temperatureIndex = 1 # temperature per hour index start at 2
    rainfallIndex = 9   # rainfallIndex per hour index starts at 9
    
    newRowList = []
    newRowList.append(key_list)
    
    
    
    for index,row in df.iterrows():
        
        print("DEBUG -1: index ",index,df.iloc[index][fields.date])
        
        
        if isFirst == True:
            if df.iloc[index-1][fields.date] == row[fields.date]:
                print("DEBUG 0: index ",index-1,df.iloc[index-1][fields.date])
                # if this date is same to the previous
                # create the new data list for appending in a row
                
                
                
                
                if firstTimeDateAdded == False:                                         # if date already added as we group by date 
                    
                    addToTempList(tempList
                                  ,index1=0
                                  ,index1Val=row[fields.date]
                                  ,index2=temperatureIndex 
                                  ,index2val=row[fields.temperature]
                                  ,index3=rainfallIndex
                                  ,index3val=row[fields.rainfall])
                    
                    print("DEBUG 1: index ",rainfallIndex,temperatureIndex)
                    
                    firstTimeDateAdded = True                                           # yes date added this time  
                
                else:
                    print("DEBUG 2: index ",rainfallIndex,temperatureIndex)
                    addToTempList(tempList,index2=temperatureIndex,index2val=row[fields.temperature],index3=rainfallIndex,index3val=row[fields.rainfall],closeblock=[0,-1,-1])                                 # don't add the date : first block closed
                    
                
                temperatureIndex +=1                                                   # increment every time up to 6 times to set 6 rows in 6 fields 
                rainfallIndex+=1                                                       #                        "
                
                
            else:
                
                newRowList.append(tempList)
                
                tempList =[]
                firstTimeDateAdded = False
                
                tempList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                temperatureIndex = 1                                    # temperature per hour index start at 2, starting at 0 index
                rainfallIndex = 9                                       # rainfallIndex per hour index starts at 10,starting at  0 index
                
                addToTempList(tempList,index1=0,index1Val=row[fields.date],index2=temperatureIndex,index2val=row[fields.temperature],index3=rainfallIndex,index3val=row[fields.rainfall])
                print("DEBUG 3: index ",rainfallIndex,temperatureIndex)
                
                temperatureIndex +=1                                                   # increment every time up to 6 times to set 6 rows in 6 fields 
                rainfallIndex+=1                                                       #                        "
                
            print(tempList)
        
        else:
            # first time adding the date 
            # and adding the temperature ,rainfall
            
            tempList[0] = row[fields.date]                                              # added date field 1 time
            tempList[temperatureIndex] = row[fields.temperature]                        # added temperatures 1 time
            tempList[rainfallIndex] = row[fields.rainfall]                              # added rainfall  1 time
            
            temperatureIndex +=1                                                        # increment every time up to 6 times to set 6 rows in 6 fields 
            rainfallIndex+=1
            
            isFirst = True 
            
        
      

        
    
    
    
if __name__ == "__main__":
    __main__()
    




# =============================================================================
#  working psudocode
#  1. read normalized data 
#      i. indented for each date
#      ii. 6 for each date
#  2. for each date group data
#  3. make new fields 
#  4. set indented data to new fields
#  
# =============================================================================

# =============================================================================
# 
# config = (Config()).getConfig()
# data = pd.read_csv(config['file'])
# df = pd.DataFrame(data)
#                 
# df.sort_values(["date",'hour'], axis = 0, ascending = True,inplace = True, na_position ='last') 
# 
# 
# =============================================================================


# make flat
