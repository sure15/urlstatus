#coding=utf-8
import urllib2
import socket
import re

def openfile(file):
    #读取文件，每行一个作为列表
    data=open(file,'r').readlines()
    #去除\n http:// /
    for x in range(len(data)):
        data[x] = data[x].replace('\n','')
        data[x] = data[x].replace('http:','')
        data[x] = data[x].replace('/','')
    print data
    return data
def openurl(url):
    try:
        ip = socket.gethostbyname(url)
        print ip,url
        return ip
    except:
        print 'failed,%s.' % url

def writefile(data):
    file=open('results.txt','a')
    file.write(data)
    file.write('\n')
    file.close()

if __name__=='__main__':
    data=openfile('url1.txt')
    for x in data:
        result=openurl(x)
        if result:
            writefile(result)
        else:
            writefile('failed')

    print len(data)