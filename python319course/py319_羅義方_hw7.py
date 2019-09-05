import requests as rq
from bs4 import BeautifulSoup
movieres = rq.get('https://movies.yahoo.com.tw/movieinfo_main/%E4%B8%8B%E5%8D%8A%E5%A0%B4-we-are-champions-9807').text
htmlmovie = BeautifulSoup(movieres, 'lxml')
a=htmlmovie.select('.movie_intro_info_r')[0].text
b=htmlmovie.select('#story')[0].text
c = a+b
file = open('movie.txt', 'w', encoding = 'UTF-8')
print(c)
file.write(c)
file.close()
