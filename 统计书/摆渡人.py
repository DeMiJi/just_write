import jieba
import matplotlib.pyplot as plt
from pylab import mpl

#解决中文乱码
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

counter = {}
txt = open("月亮与六便士.txt", "r", encoding='utf-8').read()
t = jieba.lcut(txt)
for word in t:
    if len(word) <2:
        continue
    else:
        counter[word] = counter.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1

counter_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)

print(counter_list[:50])

label = list(map(lambda x: x[0], counter_list[:50]))
value = list(map(lambda y: y[1], counter_list[:50]))

plt.bar(label, value,color = "#FF69B4",label="字",edgecolor = "#F0F8FF")
plt.tick_params(labelsize=5)
plt.xlabel('词语',fontsize = 20)
plt.ylabel('次数',fontsize = 20)
plt.title("统计月亮与六便士前50的中文词组")
plt.legend()
plt.show()