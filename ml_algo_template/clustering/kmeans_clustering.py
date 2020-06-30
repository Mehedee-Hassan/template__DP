# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:02:54 2020

@author: mehedee
@description:
    3 clusters
    then the results will be lik ethis
    we would be needing of running kmeans algorithm
    we need a way to find     

"""
#%reset -f

#importing the library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = "C:\\Users\\mehedee\\Documents\\Python Scripts\\tutorial\\Artificial_Neural_Networks\\ML_DS\\clustering\\"

# import the data set with pandas

dataset = pd.read_csv(path+'Mall_Customers.csv')

X = dataset.iloc[:,3:].values

# optimal number of clusetr : using elbo method

from sklearn.cluster import KMeans

wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter= 300,n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

print(wcss)
plt.plot(range(1,11,1),wcss)
plt.title('The Elbow Methods')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# appling k-means to the mall dataset

kmeans = KMeans(n_clusters= 5,init = 'k-means++',max_iter=300,n_init=10,random_state=0)
y_kmeans = kmeans.fit_predict(X)

temp = X[y_kmeans==0,0]
# visualising the clusters

plt.scatter(X[y_kmeans==0,0],X[y_kmeans == 0,1], s =100,c='red',label='cluster 1')
plt.scatter(X[y_kmeans==1,0],X[y_kmeans == 1,1], s =100,c='blue',label='cluster 2')
plt.scatter(X[y_kmeans==2,0],X[y_kmeans == 2,1], s =100,c='cyan',label='cluster 3')
plt.scatter(X[y_kmeans==3,0],X[y_kmeans == 3,1], s =100,c='green',label='cluster 4')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans == 4,1], s =100,c='magenta',label='cluster 5')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='centroids')
plt.title("Clusters of Clients")
plt.xlabel("Annual Income (KS)")
plt.ylabel("Spendng Score (1-100)")
plt.legend() 

plt.show()


aa= [[71,2,55,24],
     [4,5,6,7],
     [8,8,3,4]]

aapd = pd.DataFrame(aa)
print(aapd.iloc[1:,:])



print(type(dataset))



