# Neusoft2018clusterProject
    
    
该文档分三部分，第一部分是文本采集，第二部分分词与权重设置，第三部分会对文档进行聚类   
   
1、文本采集  

利用网络爬虫的方式，爬取知网论文SCI中文医学期刊对应全文关键词为“T检验”的论文摘要，一共178篇。每篇摘要对应存储为  
一个txt文件，作为本项目的文本，用于后续的分析。

2、分词与权重

files文件夹中存放的是论文库。   
在第一部分中，首先对文档进行了分词处理（采用结巴分词）。文档中的医学术语库和停用词库都是为分词所准备的    
接着，基于TF-IDF，采用了两种权重提取方式。两种方式分别为两个py文件“论文权重”和“权重提取2”   
运行不同的提取文件，都会生成相应的“key”和“dataresult”（在result文件夹中）这两个文件将会在第二部分聚类中被使用。        


3、聚类   

应用到上一步分词得到的权重矩阵，运行“数据格式转化”可以将其转化成数据框格式，得到pydata文件，其中每一行代表一个文档，
每一列代表一个关键词。读取pydata文件并命名为data作为聚类的输入。  
在聚类部分，我们采用Kmeans聚类方法，距离度量应用的是sklearn包中KMeans函数默认的欧式距离。首先通过轮廓系数选择K值，  
选择最大的轮廓系数对应的K值。然后进行聚类。  
得到聚类结果后，取出各个文档对应的类别标签，将同一类的论文整合到一个txt文件中，命名为cluster_i存在result文件夹中，  
方便后续查看和分析。

