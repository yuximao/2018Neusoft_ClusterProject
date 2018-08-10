
# coding: utf-8

# In[4]:


from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from Bio.Cluster import kcluster
from Bio.Cluster import clustercentroids
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import numpy as np
import pandas as pd
import os


# In[26]:


data=pd.read_csv('result/dfdata.csv',encoding='gb2312')
#data.drop(['Unnamed: 0'],axis=1,inplace=False)
data.head()


# In[27]:


#用轮廓系数选择K值
coef = []
x=range(2,10)
for clusters in x:
    clusterid, error, nfound = kcluster(data, clusters, dist='u',npass=100)
    silhouette_avg = silhouette_score(data, clusterid, metric = 'cosine')#
    coef.append(silhouette_avg)
  
e=[i+3 for i,j in enumerate(coef) if j == max(coef)]
print (e)
print (coef)
plt.plot(x,coef)
plt.show()


# In[28]:


num_clusters = 5
km_cluster = KMeans(n_clusters=num_clusters, max_iter=300, n_init=1, init='k-means++',n_jobs=1).fit(data)


# In[29]:


label=km_cluster.labels_
for i in range(0,num_clusters):
    data[label==i].to_csv("x"+str(i)+".csv",encoding='gb2312')


# In[32]:


index=[]
for i in range(0,num_clusters):
    print(i)
    a=data[label==i].index
    print(a)
    index.append(list(a))


# #### 将聚类结果同一类的论文合并成一个文件

# In[34]:


#获取目标文件夹的路径
filedir = os.getcwd()+'/files-2'
print(filedir)


# In[35]:



#获取目标文件夹的路径
filedir = os.getcwd()+'/files-2'

#获取当前文件夹中的文件名称列表  
#filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
for i in range(0,num_clusters):
    f=open('result/cluster_'+str(i)+'.txt','w')
    #获取相应类别的文件名称列表
    filenames=[]
    print(index[i])
    for j in index[i]:
        newname='{:0>3d}'.format(j+1)
        filenames.append(newname+'.txt')
        
    print(filenames)
    
#先遍历文件名
    for filename in filenames:
        filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
        #line=open(filepath,'w')
        #f.writelines(line)
        f.write(filename)
        f.write('\n')
        for line in open(filepath):
            f.writelines(line)
        f.write('\n')
#关闭文件
    f.close()

