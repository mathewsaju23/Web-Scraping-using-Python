import urllib
from urllib import request
from bs4 import BeautifulSoup

url = input('Enter the url (like http://py4e-data.dr-chuck.net/comments_891349.html)- ')
html = request.urlopen(url).read()

li=list()
count=0
x=BeautifulSoup(html,"html.parser")

tags=x('span')
for tag in tags:
  count=count+1
  c=int(tag.contents[0])
  li.append(c)
print('Count',count)
print('Sum =',sum(li))