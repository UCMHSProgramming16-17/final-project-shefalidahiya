import requests

base_url = 'http://isithackday.com/arrpi.php?'
par1 = 'text= '
val1= input("Talk to me ")
par2= 'format='
val2= 'json'
url = base_url + par1 + val1 + '&' + par2 + val2

print(url)

r = requests.get(url)
# get status code of r
print(r)
arr = r.json()

print(arr['translation']['pirate'])
