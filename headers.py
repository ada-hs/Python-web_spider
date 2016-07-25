__author__ = 'Ada'
import urllib.request
'''urllib中的parse用来对url解析'''
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.google.com/'
content = input("你想翻译什么呀?")
head={}
head['User-Agent']= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'


data = {}
data['type']='AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

"""修改header模拟正常浏览器的访问"""
'''response = urllib.request.urlopen(url, data)'''

'''通过Request.add_header()方法动态修改'''
req = urllib.request.Request(url,data)
req.add_header('User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')
response = urllib.request.urlopen(req)

html=response.read().decode('utf-8')

target =json.loads(html)

print("翻译结果是：%s" %(target['translateResult'][0][0]['tgt']))


