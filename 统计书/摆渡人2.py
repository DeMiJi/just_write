import jieba

txt = open("摆渡人.txt", encoding="utf-8").read()
#加载停用词表
stopwords = [line.strip() for line in open("停用词表.txt",encoding="utf-8").readlines()]
#停用词：停用词是指在信息检索中，为节省存储空间和提高搜索效率，在处理自然语言数据（或文本）之前或之后会自动过滤掉某些字或词，这些字或词即被称为Stop Words（停用词）
words  = jieba.lcut(txt)
counts = {}
for word in words:
    #不在停用词表中
    if word not in stopwords:
        #不统计字数为一的词
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(30):
    word, count = items[i]
    print ("{:<10}{:>7}".format(word, count))
