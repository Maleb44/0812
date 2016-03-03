# -*- coding: utf-8 -*-

import codecs
from bs4 import BeautifulSoup
def read_file_contents(path):
    with codecs.open(path,encoding='utf-8') as infile:
        return infile.read().strip()
    

uralkodok_str = read_file_contents("kiralyok.html")

soup=BeautifulSoup(uralkodok_str, "html.parser")
list_h3=soup.find_all('h3')
print type(list_h3)
print str(len(list_h3))
korszakok=[]
for h3 in list_h3:
    span = h3.find_all('span',{'class':'mw-headline'})
    if span:
      # print span
        korszak = h3.a['title']
        print korszak
        table = h3.next_sibling.next_sibling
        print table
        korszakok.append(korszak)

print korszakok
print korszakok[0]
print korszakok[1]


#      korszak = span.text
#      korszak = span.title
#        table = h3.next_sibling.next_sibling    ### ,find('tr')
#        korszakok.append((korszak,table))
#        print '----'

        
