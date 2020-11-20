#导入词云的包
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
#导入matplotlib作图的包
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.colors as colors

#读取文件,返回一个字符串，该文档位于此python同以及目录下
f = open('introduction.txt','r').read()

background_Image = np.array(Image.open("TiDB-logo.jpg"))

colormaps = colors.ListedColormap(['#E36209','#E6b949','#CCAC55','#A5D10D','#127d72'])

#生成一个词云对象
wordcloud = WordCloud(
        background_color="white", #设置背景为白色，默认为黑色
        font_path="Ubuntu-Medium.ttf",
        stopwords = STOPWORDS.add("store"),
        mask=background_Image,
        colormap = colormaps,
        width=1400,              #设置图片的宽度
        height=900,              #设置图片的高度
        margin=10,               #设置图片的边缘
        relative_scaling=0.3
        ).generate(f)
# 绘制图片
plt.imshow(wordcloud)
# 消除坐标轴
plt.axis("off")
# 展示图片
# plt.show()
# 保存图片
wordcloud.to_file('my_test4.png')