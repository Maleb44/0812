# request
import requests

#print r
#
#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#print(r.url)
#print r.status_code
#
r = requests.get('https://hu.wikipedia.org/wiki/Kezd%C5%91lap')
print(r.url)
print r.status_code
print r.text
print r.encoding  # UTF-8
