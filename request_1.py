# request
import requests
import codecs
import json

def read_json(path):
    with codecs.open(path,encoding='utf-8') as infile:
        return json.loads(infile.read())

def write_json(path,data):
    with codecs.open(path,'w',encoding='utf-8') as outfile:
        json.dump(data.outfile,indent=2,ensure_ascii=False,sort_keys=True)




r1 = requests.get('http://paste.ee/r/laxjw')
print type(r1)
read_json('r1')

#if r1.status_code:
    
