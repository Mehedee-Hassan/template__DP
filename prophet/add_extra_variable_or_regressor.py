import pandas as pd
df = pd.DataFrame(pd.date_range(start="2019-09-01", end="2019-09-30", freq='D', name='ds'))
df["y"] = range(1,31)
df["add1"] = range(101,131)
df["add2"] = range(201,231)
df.head()
"""
            ds  y   add1 add2
0   2019-09-01  1   101 201
1   2019-09-02  2   102 202
2   2019-09-03  3   103 203
3   2019-09-04  4   104 204
4   2019-09-05  5   105 205"""

# split train and test set
df_train = df.loc[df["ds"]<"2019-09-21"]
df_test  = df.loc[df["ds"]>="2019-09-21"]



#

from fbprophet import Prophet
m = Prophet()
m.add_regressor('add1')
m.add_regressor('add2')
m.fit(df_train)

forecast = m.predict(df_test.drop(columns="y"))


# source 
# https://stackoverflow.com/questions/54544285/is-it-possible-to-do-multivariate-multi-step-forecasting-using-fb-prophet