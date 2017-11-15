Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> values={}
>>> values['username'] = "809386174@qq.com"
>>> values['password'] = "shenxiaoting"
>>> data = urllib.urlencode(values)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data = urllib.urlencode(values)
NameError: name 'urllib' is not defined
>>> data = urllib.urlencode(values)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data = urllib.urlencode(values)
NameError: name 'urllib' is not defined
>>> url = "http://passport.csdn.net/account/login"
>>> geturl = url + "?"+data

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    geturl = url + "?"+data
NameError: name 'data' is not defined
>>> request = urllib2.Request(geturl)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    request = urllib2.Request(geturl)
NameError: name 'urllib2' is not defined
>>> response + urllib2.urlopen(request)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    response + urllib2.urlopen(request)
NameError: name 'response' is not defined
>>> print response.read()

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print response.read()
NameError: name 'response' is not defined
>>> 
