import urllib.request
import random

url ='http://www.whatismyip.com.tw'

iplist=['111.12.83.65','112.5.220.199','61.135.217.12']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

'''
proxy_support = urllib.request.ProxyHandler({'http':'112.5.220.199:80'})'''
    

opener = urllib.request.build_opener(proxy_support)
    
urllib.request.install_opener(opener)
    
response = urllib.request.urlopen(url)
    
html = response.read().decode('utf-8')
    
print (html)
