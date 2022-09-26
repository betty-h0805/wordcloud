# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np


jieba.load_userdict('dict.txt')

hash = {}   #創建一個字典
for t in range (1,15) :   #爬取1-15頁的資料
    url = 'https://technews.tw/category/internet-of-things-internet/page/'+str(t)
    r = requests.get(url)
    response = r.text
    soup = bs(response,'lxml')
    
    href = soup.find_all('a',rel = 'bookmark')   #找到頁內超連結
    #取出內文
    for k in href :
        t1 = k.get('href')
        t1 = 'https:' + t1 if t1[0] == '/' else t1
        
        
        r = requests.get(t1)
        soup = bs(r.text,'lxml')
        content = soup.select('.indent>p')
        
        #將內文轉成文字
        article = []
        for c in content:
            
            article.append(c.text)
        articleAll = '\n'.join(article)   #每行合併，即獲得所有要爬取的文字
        
        #設定高頻率出現的詞，之後進行過濾
        stopwords = {}.fromkeys(["也","但","來","個","再","的","和","是","有",'於','為','都','而','能','：','《','》',"更","會","可能","有何","從","對","與","等","、","了","就", '卻','不過','時','\n','越','為','這種','多','越來','在','你','我','他','說',' ','，','。','（','）','！','？'])

        Sentence = jieba.cut_for_search(articleAll) 
        
        # 計算stopwords之外的詞頻
        
        for item in Sentence:
            if item in stopwords:
                continue
            elif item in hash:
                hash[item] += 1
            else:
                hash[item] = 1

font = "C:\\Windows\\Fonts\\AdobeFanHeitiStd-Bold.otf"


wc = WordCloud(font_path = font,         #設定字型
               background_color="white", #背景顏色
               max_words = 2000 ,        #文字雲顯示最大詞數
               stopwords=stopwords)      #停用字詞
wc.generate_from_frequencies(hash)

#印出結果
plt.imshow(wc)
plt.axis("off")
plt.figure(figsize=(20,10), dpi =200)
plt.show()

wc.to_file('wordcloud.jpg')    #以.jpg輸出