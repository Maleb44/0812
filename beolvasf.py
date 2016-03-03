# -*- coding: utf-8 -*-

import codecs
from bs4 import BeautifulSoup
def read_file_contents(path):
    with codecs.open(path,encoding='utf-8') as infile:
        return infile.read().strip()
    
#kiralyok_html ='uralkodok.html'

#  outp = read_file_contents("test.txt")

uralkodok_str = read_file_contents("kiralyok.html")

#type (outp)
#print str(len(outp))
soup=BeautifulSoup(uralkodok_str)
list_h3=soup.find_all('h3')
#print list_h3
print str(len(list_h3))
#print list_h3[0]
#print list_h3.span
for h3 in list_h3:
    span = h3.find_all('span',{'class':'mw-headline'})
    #span = h3.find('span', {'class':'mw-headline'})
    
   # print span
   # print '#############'
    
    if span:
        print 'kkkkkkkkkkkkkkkkkk'
        print span
        print type(span)
     #   span.attr
      #  korszak = span.a.text

        '''
        print span
        print '---------'
        
        
      
        korszak = span.text
     #   korszak = span.title
        table = h3.next_sibling.next_sibling    ### ,find('tr')
        korszakok,append((korszak,table))
        print '----'
        '''
# print list_h3[0].span

