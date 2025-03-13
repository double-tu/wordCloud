# coding:utf-8

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def generate_wordcloud(text, priorities=None):
    '''
    输入文本生成词云，不进行分词处理
    Args:
        text: 输入文本，用逗号分隔的词语
        priorities: 词语优先级字典，格式为{'word': priority_value}
    '''
    # 设置显示方式
    d=path.dirname(__file__)
    alice_mask = np.array(Image.open(path.join(d, "Images//tree.png")))
    font_path=path.join(d,"font//msyh.ttf")
    stopwords = set(STOPWORDS)
    
    # 将文本按逗号分割并转换为词频字典
    words = [word.strip() for word in text.split(',')]
    word_freq = {word: words.count(word) for word in set(words)}
    
    # 应用优先级
    if priorities:
        for word, priority in priorities.items():
            if word in word_freq:
                word_freq[word] = priority
    
    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words=2000, # 词云显示的最大词数
           mask=alice_mask,# 设置背景图片
           stopwords=stopwords, # 设置停用词
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
           repeat=True, # 允许词重复
                  )

    # 生成词云
    wc.generate_from_frequencies(word_freq)

    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, "Images//alice.png"))

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    plt.axis("off")# 关掉图像的坐标
    plt.show()

