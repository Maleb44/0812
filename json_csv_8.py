import json
import csv

#out_f = open ('data_t6.cvs','w') 




cnt =0
with open('data.json') as data_file:    
    data = json.load(data_file)   
    print str(len(data))
    print type(data)
    
    with open('data_t8.csv', 'w') as csvfile:
        fieldnames = ['name', 'creditcard']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
        writer.writeheader()
        
        for elem in range (10):
            
            if data[elem]['creditcard'] != None:
                writer.writerow({'name': data[elem]['name'], 'creditcard': data[elem]['creditcard']})
                cnt +=1
print "hitelkartyak szama:" + str(cnt)            
csvfile.close ()
data_file.close()

                    
