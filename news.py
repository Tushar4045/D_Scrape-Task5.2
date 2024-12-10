import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

newsUrl = 'https://www.ft.com/stream/7e37c19e-8fa3-439f-a870-b33f0520bcc0'
newsHeader = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
newsResp = rq.get(url=newsUrl, headers=newsHeader)
newsSoup = BeautifulSoup(newsResp.content,'html.parser')

newsTime = newsSoup.find_all('time')
time = [time['datetime'] for time in newsTime]

newsHeading = newsSoup.find_all('div',attrs={'class':"o-teaser__heading"})
heading = [heading.text for heading in newsHeading]

newsContent =  newsSoup.find_all('p',attrs={'class':"o-teaser__standfirst"})
content = [content.text for content in newsContent]

newsData = {
    'Time':time,
    'Heading':heading,
    'Content':content
}
df = pd.DataFrame(newsData)
newsDataDF = df.replace({r'[“”‘’]': '"'}, regex=True)
newsDataDF.to_csv('news.csv', encoding='utf-8', index=False)
