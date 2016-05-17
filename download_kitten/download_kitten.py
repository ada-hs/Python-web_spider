__author__ = 'Ada'
import urllib.request
req = urllib.request.Request("http://placekitten.com/500/600")
response = urllib.request.urlopen(req)
kitten_img = response.read()
with open('kitten_img.jpg','wb') as f:
    f.write(kitten_img)
response.geturl()
response.info()
print (response.getcode())

