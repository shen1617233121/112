import urllib2
import re

url = 'http://b2b.11467.com/search/-4fe1606f6280672f.htm'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(req)
html = response.read().decode('utf-8')
with open('D:/test.html','wb') as f:
    f.write(response.read())
    f.close()
'''
content_pattern = re.compile('<span class="bianhao">.*?</span>.*?<a.*?>(.*?)</a>', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item




content_pattern = re.compile('<span class="bianhao">.*?</span>.*?<div>(.*?)</div>', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item




content_pattern = re.compile('<span class="bianhao">.*?</span>.*?<div>.*?<div>(.*?)</div>', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item


content_pattern = re.compile('<span class="bianhao">.*?</span>.*?<div>.*?<div>.*?<div>(.*?)</div>', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item
'''
all_pattern = re.compile('<span class="bianhao">.*?</span>.*?<a.*?>(.*?)</a>.*?<span class="bianhao">.*?</span>.*?<div>(.*?)</div>.*?<span class="bianhao">.*?</span>.*?<div>.*?<div>(.*?)</div>.*?<div>(.*?)</div>',re.S)
all_list = re.findall(all_pattern, html)
for item in all_list:
    print "name:" + item[0]
    print "title:" + item[1]
    print "content:" + item[2].strip()
    print "good:" + item[3]
    print "-----------------"

    input = raw_input()
    if input == "":
        print "nextPage:"
        continue
    elif input =="Q":
        break
