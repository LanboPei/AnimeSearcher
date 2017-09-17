import urllib
import urllib.request
import time
import sys

'''
Time Measurement
http://www.jb51.net/article/63244.htm
https://docs.python.org/3/library/time.html#time.time

urllib(.request(.urlopen))
https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen

'''

start = time.time()

url = "http://bangumi.tv/subject/10380" #这里是需要获取的网页
content = urllib.request.urlopen(url).read() #使用urllib模块获取网页内容
##print(content) #输出网页的内容 功能相当于查看网页源代码


c = content.decode()
print(type(c))
print(c[45:450])

sys.exit()

with open("result.txt", "wb") as f:
    f.write(content)

rt = time.time() - start
print(rt)
