
# coding: utf-8

# In[64]:


import numpy as np
from sklearn.cluster import KMeans
import pandas as pd


# In[77]:


#读取TF-IDF权重矩阵——dataresult，并转化成数据框格式
data=pd.read_table("result/dataresult.txt",header=None)
data.drop([1423],axis=1,inplace=True)
data.head()


# In[78]:


#读取关键词
file=open("result/key.txt", encoding="gbk").read()


# In[79]:


ikey=[]
for i in range(0,data.shape[1]):
    ikey.append(file.split(',')[i])


# In[80]:


#将关键词作为权重矩阵的列名
data.columns=ikey
data.head()


# In[81]:


#生成csv数据存储起来，方便后续读取
data.to_csv("result/dfdata.csv",encoding="gb2312")

