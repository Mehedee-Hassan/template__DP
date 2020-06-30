# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


path = "C:\\Users\\mehedee\\Documents\\Python Scripts\\tutorial\\Artificial_Neural_Networks\\ML_DS\\"
file_name = 'Market_Basket_Optimisation.csv'

# Data Preprocessing
dataset = pd.read_csv(path+file_name, header = None)

transactions =[]

for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])


from apyori import apriori

rules = apriori(transactions ,min_support=0.003 ,min_confidence=0.2 ,min_lift=3,min_length=2)


results = list(rules)
againlist= []
print(results)
i = 0
for result in results:
    againlist.append(str(result))
    
    #againlist.append(str(list(*result)))



# suppor: products that are purchased more frequently at least 3-4 times a day
    #-  let the product 3 times a day : -- 3*7 / 7501
#-  confidance of 0.8 means the rules have to be correct for 80% of times
    #- that is 4 out of 5 times the rules have to be correct
#- minimum lift 
    # - Lift(A→B) = (Confidence (A→B))/(Support (B))
    # - Confidence(A→B) = (Transactions containing both (A and B))/(Transactions containing A)
    # -Support(B) = (Transactions containing (B))/(Total Transactions)
# source : https://stackabuse.com/association-rule-mining-via-apriori-algorithm-in-python/




"""
@NOTE:explanation of preparing feature data for apriory algo
    
aa = {'a':[1,2,3,4,5,6],'b':[31,42,32,44,65,76],'n':[301,142,232,444,365,276]}
aa = pd.DataFrame(aa)

print([aa.values[0,j] for j in range(0,3)])
"""

