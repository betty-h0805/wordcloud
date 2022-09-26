# Wordcloud
## Introduction
This is a simple program which can find out some frequently used words in technology news and visualize the result.
## Target
By generating the wordcloud, we can quickly find out some popular topics.
## Python library in need
+ `BeautifulSoup` `jieba`
+ `request`
+ `matplotlib` `wordcloud` 
+ `PIL`
+ `numpy`
## Technique
1. Use the concept of WebRequest and obtain the pure text of news articles
2. Use `jieba` to seperate sentences into words
3. Filter some stopwords
4. Calculate the frequency of each words
5. Generate a wordcloud which display most frequently used words.
## Result
![圖片](https://user-images.githubusercontent.com/57898179/192297126-af7ebe7f-4a9b-4b88-82f9-a87ec208b35d.png)

## Future Work
+ Filter stopwords more precisely
+ Transform the wordcloud into diverse shape
