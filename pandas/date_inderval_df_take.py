#set the dataframe date coloumn to index coloumn

df_test_holiday = df_holiday.copy()
df_test_holiday=df_test_holiday.set_index('date')

# convert the index coloumn to datetime

df_test_holiday.index = pd.to_datetime(df_test_holiday.index)

df_test_holiday=df_test_holiday[df_test_holiday.index >=pd.to_datetime(dt.strptime('2016-07-21','%Y-%m-%d'))]
print(df_test_holiday.index[0]) 
# start date should be '2016-07-21'


df_test_holiday=df_test_holiday[df_test_holiday.index <=pd.to_datetime(dt.strptime('2020-04-29','%Y-%m-%d'))]
print(df_test_holiday.index[len(df_test_holiday)-1]) 
# end date should be '2020-04-29'



