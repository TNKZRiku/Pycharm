import os
import time
import jieba
import numpy
from PIL import Image
from wordcloud import WordCloud
import re

pat = re.compile(r'^[\u4e00-\u9fff]')
lst = []
img = Image.open('D:/homework_files/wordcloudEF-pic.png')
mask = numpy.array(img)
jieba.add_word('乃爱')

with open('D:/homework_files/tenshisouzou.txt','r',encoding = 'utf-8') as f:
    for line in f:
        line = re.sub(pat, '', line)

        words = jieba.lcut(line)
        lst.extend(w for w in words if len(w) > 1)
        text = ' '.join(lst)

    wc = WordCloud(
        background_color = 'white',
        max_words = 300,
        prefer_horizontal = 1,
        font_step = 0.3,
        font_path = 'msyh.ttc',
        height = 1920,
        width = 2560,
        mask = mask,
        colormap = 'coolwarm'
    )
    wc.generate(text)
    wc.to_file('D:/homework_files/tenshouzou.png')
    time.sleep(0.5)
    os.startfile('D:/homework_files/tenshouzou.png')


