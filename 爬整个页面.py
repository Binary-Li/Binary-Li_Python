#utf-8
from urllib import request
A=request.urlopen("http://www.baidu.com")
print(A.read()) 