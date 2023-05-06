# -*- coding: utf-8 -*-
"""customer segmentation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NvbetoN77XTDueh7xFY0BGCcZOzbi6Kd
"""



"""Importing the dependencies"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

"""Data collection and analysis

"""

customer_data = pd.read_csv('/content/Mall_Customers.csv')

customer_data.head()

#finding the number of rows and columns
customer_data.shape

#Getting some information about the dataset
customer_data.info()

#checking for the missing values
customer_data.isnull().sum()

"""Choosing the annual income column and spending score column"""

x = customer_data.iloc[:,[3,4]].values

print(x)

"""Choosing the number of clusters
wcss ->within clusters sum of squares
"""

#finding wcss value for fifferent number of clusters
wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)

#plot an elbow graph
sns.set()
plt.plot(range(1,11), wcss)
plt.title('The elbow point graph')
plt.xlabel('number of clusters')
plt.ylabel('wcss')
plt.show()

"""Optimum number of clusters=5

training the k-means clustering model
"""

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=0)
#return a label for each data point based on cluster
y = kmeans.fit_predict(x)
print(y)

"""Visualizing all the clusters"""

#plotting all the clusters and their centroids
plt.figure(figsize=(8,8))
plt.scatter(x[y==0,0], x[y==0,1], s=50, c='green', label='cluster 1')
plt.scatter(x[y==1,0], x[y==1,1], s=50, c='red', label='cluster 2')
plt.scatter(x[y==2,0], x[y==2,1], s=50, c='blue', label='cluster 3')
plt.scatter(x[y==3,0], x[y==3,1], s=50, c='yellow', label='cluster 4')
plt.scatter(x[y==4,0], x[y==4,1], s=50, c='violet', label='cluster 5')

#plot the centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='cyan', label='centroids')
plt.title('customer groups')
plt.xlabel('annual income')
plt.ylabel('spending score')
plt.show()