# -*- coding: utf-8 -*-


#      korszak = span.text
#      korszak = span.title
#        table = h3.next_sibling.next_sibling    ### ,find('tr')
#        korszakok.append((korszak,table))
#        print '----'

        
f = open("datajson.txt")
i = 0
try:
    for line in f:
        print line
        i +=1
        print str(i)
finally:
    f.close
