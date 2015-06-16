#coding=utf-8
import urllib2
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
        url1=url
        url='http://whois.chinaz.com/'+url+'&isforceupdate=1'
        connection=urllib2.urlopen(url).read()
        pattern = re.compile(r'注册商：(.*?), LLC')
        data = re.findall(pattern,connection)
        if not data:
            data = ['hichina']
        print data[0],url1
        return data[0]
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