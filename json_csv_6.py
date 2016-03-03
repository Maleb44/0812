import json


out_f = open ('data_t6.csv','w') 


import json
#import readline
cnt =0
with open('data.json') as data_file:    
    data = json.load(data_file)   
    print str(len(data))
    print type(data)
    el  = data[0]
    print el
    
    for elem in range (len(data)):
        if data[elem]['creditcard'] != None:
         #   print  data[elem]['name'] +',' + data[elem]['creditcard']
            print >> out_f, (data[elem]['name'] +',' + data[elem]['creditcard'])
            cnt +=1
print "hitelkartyak szama:" + str(cnt)            
out_f.close ()
data_file.close()

