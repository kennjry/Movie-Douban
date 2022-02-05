import jieba  #分词
from matplotlib import pyplot as plt #帮忙绘图的工具，数据可视化
from wordcloud import WordCloud
from PIL import Image   #图片处理
import numpy as np  #用来进行矩阵运算
import sqlite3

#查询出简介，并进行拼接
con=sqlite3.connect("move.db")
cur=con.cursor()
sql="select instroduction from movie250"
data=cur.execute(sql)
text=""
for item in data:
    text=text+item[0]
#print(text)
cur.close()
con.close()

#分词
cut=jieba.cut(text)
string=" ".join(cut) #将分好的词用空格分隔
print(len(string))   #有5462个词

img=Image.open(r'.\static\assets\img\tree.jpg')   #打开遮罩图片
img_array=np.array(img)    #将图片转换为数组
wc=WordCloud(
    background_color='white',
    mask=img_array,
    font_path="ARIALUNI.TTF"  #在C:\Windows\Fonts中可以查看字体样式
)
wc.generate_from_text(string)

#绘制图片
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off') #不显示坐标轴

#plt.show()   显示生成的词云图片

#输出词云图片到文件
plt.savefig(r'.\static\assets\img\word.jpg',dpi=500)  #dpi表示清晰度