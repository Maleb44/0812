import json

## csv file
out_f = open ('data_t4.csv','w') 

## json file
import json
with open('data.json') as data_file:    
    data = json.load(data_file)   
    print str(len(data))
    cnt=0
    for i in range (len(data)/10):
    #    print i
        a_elem = data [i]
        hitelkartya = a_elem['creditcard']
        cnt +=1
        nev = a_elem['name']
         #   sor = str(nev) + ',' + str(hitelkartya) 
        sor = str(nev) + ',' + str(hitelkartya) + '\n'
         #   print sor
        out_f.write(sor)
print "hitelkartyak szama:" + str(cnt)            
out_f.close ()
data_file.close()
#pprint(data)
