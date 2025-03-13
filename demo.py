# coding:utf-8

from os import path
import chnSegment
import plotWordcloud


if __name__=='__main__':

    # 读取文件
    d = path.dirname(__file__)
    #  text = open(path.join(d, 'doc//十九大报告全文.txt')).read()
    text = open(path.join(d,'doc//xz.txt'), encoding='utf-8').read()
    #  text="付求爱很帅并来到付求爱了网易研行大厦很帅 很帅 很帅"

    # 若是中文文本，则先进行分词操作
    # text=chnSegment.word_segment(text)
    priorities = {
    'To grow like a tree': 100,
    '厚德 博学 笃行 健美': 90,
    '30th birthday': 80,
    'Rainbow English': 70,
    '17所成员校': 65,
    '彩虹英语': 60,
    'chase dreams': 60,
    'grow deep roots': 60,
    'reach for the sky': 60
}
    
    # 生成词云
    plotWordcloud.generate_wordcloud(text, priorities)
