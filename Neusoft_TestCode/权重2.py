# encoding=utf-8
import jieba
import os
from sklearn.feature_extraction.text import TfidfVectorizer
# print(dir(TfidfVectorizer))
import jieba.posseg
from collections import Counter

jieba.load_userdict("医学名词.txt")   # 加载用户自定义词典
def cut(txt_name1, txt_name2):
    l = []
    with open(txt_name1, 'r',encoding='utf-8') as f1:    # 以只读方式打开文件
        txt = f1.read()
        txt_encode = txt.encode('utf-8')
        txt_cut = jieba.posseg.cut(txt_encode)         # 切词
        # result = ' '.join(txt_cut)

        for i in txt_cut:
            if i.flag == 'n':
                l.append(i.word)
        # print(l)
    with open(txt_name2, 'w') as f2:    # 分词结果写入文件保存
        for i in l:
            f2.write(i+' ')
    f1.close()
    f2.close()
corpus = []
rootdir = 'files'
llist = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(llist)):
    path = os.path.join(rootdir,llist[i])
    print(i,path)
    if os.path.isfile(path):
        cut(path, 'result/1-1.txt')
    # 分别对文件调用cut方法分词
        with open('result/1-1.txt', 'r') as f3:
            res3 = f3.read()
        corpus.append(res3)




# 将停用词表从文件读出，并切分成一个数组备用
stopWords_dic = open('中文停用词库.txt', 'r')     # 从文件中读入停用词
stopWords_content = stopWords_dic.read()
stopWords_list = stopWords_content.splitlines()     # 转为list备用
stopWords_dic.close()

# print(corpus)
vector = TfidfVectorizer(stop_words=stopWords_list)
tf_idf = vector.fit_transform(corpus)
# print(tf_idf)

word_list = vector.get_feature_names()      # 获取词袋模型的所有词
weight_list = tf_idf.toarray()
# result1 = ''.join(word_list)
# result2 = ''.join(weight_list)
# print(result1, result2)
# with open('files/wordslist.txt', 'w') as f3:
#     f3.write(result)
total=[] #每篇文章数据分别存入
dictt={}
mun={}
edic={}
sset=set()

# 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
for i in range(len(weight_list)):
    ddict={} #装每个文档的数据
    for j in range(len(word_list)):
        ddict[word_list[j]] = weight_list[i][j]
    edic=dict(sorted(ddict.items(), key=lambda x: x[1], reverse=True))
    setnum=0

    for k,v in edic.items():
        setnum+=1
        if setnum<=25: #每篇文章取前多少个关键词。关键词取得越多聚类维度越多，同时也会增加废话的概率
            sset.add(k)
    total.append(ddict)
dl=total[0]
namelist=list(sset)
di = []  # 非前指定key

isok = 'false'
for k, v in dl.items():
    for kk in namelist:
        if k == kk:
            isok = 'true'
            break
        else:
            isok='false'
    if isok == 'false':
        di.append(k)

for i in total:
    for k in di:
        i.pop(k)
f2=open('result/key.txt','w')
iii=0
for k in total[0]:
    f2.write(k)
    f2.write(',')
    iii+=1
print(iii)
f2.close()
fl=open('result/dataresult.txt', 'w')
for i in total:
    for k,v in i.items():
        s=str(v)
        fl.write(s)
        fl.write("\t")
    fl.write("\n")
fl.close()
# acc=0
# # for k,v in total[0].items():
# #     acc +=1
# #     print(acc,k)
