import jieba
import jieba.posseg  # 需要另外加载一个词性标注模块

string = '其实大家买手机就是看个心情，没必要比来比去的。'
seg = jieba.posseg.cut(string)

l = []
for i in seg:
    if i.flag == 'n':
        l.append(i.word)
print (l)
