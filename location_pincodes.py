import requests
f = open('places.txt', 'r')
for line in f:
        s = 'http://www.getpincode.info/api/pincode?q='+line
        r = requests.get(s)
        print r.text
