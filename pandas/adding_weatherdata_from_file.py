# code is in xgboost file


import pandas as pd


df = pd.read_csv(data_path2+datafile)
# making empty datafield
# df['temp1200h'] = list([0]*len(df))
# df['temp1800h'] = list([0]*len(df))



#adding weather data
#       => the data reading part 
weather_file_path = 'C:/Users/xx/'
weather_file_name = 'xxx_flat_16-20.csv'

#       => the comparison  part 


c = 0
last_index = 0
totallen = len (df_weather)
for index, row in df.iterrows():
    
#     if c>10 : break;c+=1;print(index.date())
    
    for index2 in range(last_index,totallen):
        if index.date()==(datetime.strptime( df_weather['date'][index2] ,'%Y-%m-%d')).date():
            df.loc[index,'temp0h'] = df_weather.loc[index2 , 'temp0h']
            df.loc[index,'temp300h'] = df_weather.loc[index2 , 'temp300h']
            df.loc[index,'temp600h'] = df_weather.loc[index2 , 'temp600h']
            df.loc[index,'temp900h'] = df_weather.loc[index2 , 'temp900h']
            df.loc[index,'temp1200h'] = df_weather.loc[index2 , 'temp1200h']
            df.loc[index,'temp1500h'] = df_weather.loc[index2 , 'temp1500h']
            df.loc[index,'temp1800h'] = df_weather.loc[index2 , 'temp1800h']
            df.loc[index,'temp2100h'] = df_weather.loc[index2 , 'temp2100h']
            
            # adding rain
            df.loc[index,'rain0h'] = df_weather.loc[index2 , 'rain0h']
            df.loc[index,'rain300h'] = df_weather.loc[index2 , 'rain300h']
            df.loc[index,'rain600h'] = df_weather.loc[index2 , 'rain600h']
            df.loc[index,'rain900h'] = df_weather.loc[index2 , 'rain900h']
            df.loc[index,'rain1200h'] = df_weather.loc[index2 , 'rain1200h']
            df.loc[index,'rain1500h'] = df_weather.loc[index2 , 'rain1500h']            
            df.loc[index,'rain1800h'] = df_weather.loc[index2 , 'rain1800h']            
            df.loc[index,'rain2100h'] = df_weather.loc[index2 , 'rain2100h']

            
            last_index = index2 
            break
            
            