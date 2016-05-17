__author__ = 'Ada'
import urllib.request
'''urllib中的parse用来对url解析'''
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.google.com/'
content = input("你想翻译�?么呀�?")

data = {}
data['type']='AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)
html=response.read().decode('utf-8')

target =json.loads(html)

print("翻译结果是：%s" %(target['translateResult'][0][0]['tgt']))


