import requests
from bs4 import BeautifulSoup
import wget


Url = 'https://bmcsystbiol.biomedcentral.com/articles'
Req = requests.get(Url)
con = Req.content
soup = BeautifulSoup(con,'html.parser')

div_titles = soup.findAll("a", {"data-test": "title-link"})

div_authors = soup.findAll("p", {"class": "c-listing__authors u-margin-bottom-0"})

li_dates = soup.findAll("span", {"itemprop": "datePublished"})

links_pdf = soup.find_all(href=True)
str = list()
for link in links_pdf:
    if("pdf" in link['href']):
        str.append('https://bmcsystbiol.biomedcentral.com'+link['href'])

# plik do zapisania danych autorow i tytulow
f = open("data.txt","w+",encoding='UTF8')

count = 0;
# count objects
for div in div_titles:
    count+=1;

for i in range (0,count):
    if("April" in li_dates[i].getText()):
        f.write('title: '+div_titles[i].getText()+"\n")
        f.write('authors: '+div_authors[i].getText()+"\n")
        f.write('date: '+li_dates[i].getText()+'\n')
        f.write('pdf '+str[i]+'\n')
        f.write('\n')
        # download
        # it will overwrite so 1 2 etc
        wget.download(str[i],'article.pdf')

f.close
