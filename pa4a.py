Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:/Users/lenovo32/Desktop/≈¿≥Ê4.py ================

Traceback (most recent call last):
  File "C:/Users/lenovo32/Desktop/≈¿≥Ê4.py", line 11, in <module>
    response = urllib2.urlopen(request)
  File "C:\Python27\lib\urllib2.py", line 154, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python27\lib\urllib2.py", line 429, in open
    response = self._open(req, data)
  File "C:\Python27\lib\urllib2.py", line 447, in _open
    '_open', req)
  File "C:\Python27\lib\urllib2.py", line 407, in _call_chain
    result = func(*args)
  File "C:\Python27\lib\urllib2.py", line 1228, in http_open
    return self.do_open(httplib.HTTPConnection, req)
  File "C:\Python27\lib\urllib2.py", line 1198, in do_open
    raise URLError(err)
URLError: <urlopen error [Errno 10060] >
>>> import urllib2
>>> urillb2.Request('http://www.baidu.com',headers={'User-Agent':user_agent})

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    urillb2.Request('http://www.baidu.com',headers={'User-Agent':user_agent})
NameError: name 'urillb2' is not defined
>>> user_agent = 'Mozilla/5.0(Windows NT 6.1:WOW64)AppleWebKit/537.36(KHTML,like Gecko) Chrome/62.0.3202.75 Safari/537.36'
>>> urillb2.Request('http://www.baidu.com',headers={'User-Agent':user_agent})

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    urillb2.Request('http://www.baidu.com',headers={'User-Agent':user_agent})
NameError: name 'urillb2' is not defined
>>> 
