__author__ = 'Ada'
import urllib.request
url = "http://www.adastaybrave.com"
response = urllib.request.urlopen(url)
html = response.read()

html = html.decode('utf-8').encode("utf-8")

print(html)


