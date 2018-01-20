import jieba.analyse
import Align
import time
import Crawl_test

# 此模块用于分析文件中的字频，输出结果形如 词语 --- 权重频次
f = open(Crawl_test.filename+'.txt', 'r', encoding='utf-8')
fcontent = f.read()

tags = jieba.analyse.extract_tags(fcontent, topK=100, withWeight=True)
new_tags = {}
for k in range(len(tags)):
    new_tags[tags[k][0]]= int(tags[k][1]*10000)

# 输出语句，注意格式化对齐的方式
with open(Crawl_test.filename + '_Word.txt', 'w') as f:
    for i,j in tags:
            f.write(i+'\n')
            # print('{:8}\t{:10}'.format(i,int(j*10000)))
    f.close()

