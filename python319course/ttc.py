import requests as rq
from bs4 import*
ntucoulink = []
j=0
for i in range(1297,1300):
    a = rq.get('https://www.ptt.cc/bbs/NTUcourse/index'+str(i)+'.html').text
    soup = BeautifulSoup(a,'html.parser')
    allist=soup.select('.title a')
    for k in range(0,len(allist)-1):
        ntucoulink = ntucoulink +[allist[k]['href']]
print(ntucoulink)
print(len(ntucoulink))
cont=[]
for link in ntucoulink:
    cont=cont+[rq.get('https://www.ptt.cc'+link).text]
print(cont)
