
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.cluster import KMeans
import pandas as pd


# In[ ]:


data=pd.read_table("result/dataresult.txt",header=None)
data.drop([1423],axis=1,inplace=True)
data.head()


# In[ ]:


file=open("result/key.txt", encoding="gbk").read()


# In[ ]:


ikey=[]
for i in range(0,data.shape[1]):
    ikey.append(file.split(',')[i])


# In[ ]:


data.columns=ikey
data.head()


# In[ ]:


data.to_csv("result/data.csv",encoding="gb2312")


# In[2]:


data=pd.read_csv('result/data.csv',encoding='gb2312')
data.head()


# In[4]:
#
# 57-80为用轮廓系数选择K值
# from sklearn.cluster import KMeans
# from sklearn.metrics import silhouette_score
# from Bio.Cluster import kcluster
# from Bio.Cluster import clustercentroids
# import matplotlib.pyplot as plt
# get_ipython().magic('matplotlib inline')
# import numpy as np


# In[22]:

#
# coef = []
# x=range(2,10)
# for clusters in x:
#     clusterid, error, nfound = kcluster(data, clusters, dist='u',npass=100)
#     silhouette_avg = silhouette_score(data, clusterid, metric = 'cosine')#
#     coef.append(silhouette_avg)
#
# e=[i+3 for i,j in enumerate(coef) if j == max(coef)]
# print (e)
# print (coef)
# plt.plot(x,coef)
# plt.show()


# In[12]:

#聚类的部分
num_clusters = 6
km_cluster = KMeans(n_clusters=num_clusters, max_iter=300, n_init=1, init='k-means++',n_jobs=1).fit(data)


# In[16]:


centers=km_cluster.cluster_centers_


# In[15]:



# In[13]:


label=km_cluster.labels_


# In[14]:


for i in range(0,num_clusters):

    data[label == i].to_csv("result/x"+str(i)+".csv",encoding="gb2312")


# #### 将同一类的论文合并成一个文件


# indexlist=data[label==1].index
# inlist=list(indexlist)
# print(inlist)
