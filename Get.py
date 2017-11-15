
import urllib
import urllib2
 
values={}
values['username'] = "809386174@qq.com"
values['password']="123456"
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.geturl()
