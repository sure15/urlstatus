#coding=utf-8
import urllib2
from multiprocessing import Pool

def openfile(file):
    #读取文件，每行一个作为列表
    data=open(file,'r').readlines()
    #去除\n
    for x in range(len(data)):
        data[x] = data[x].replace('\n','')
    print data
    return data
def openurl(url):
    try:
        connection=urllib2.urlopen(url)
        print connection.getcode(),url
        connection.close()
    except:
        print 'failed,%s.' % url


if __name__=='__main__':
    p = Pool(41)
    data=openfile('url.txt')
    for x in data:
        p.apply_async(openurl,args=(x,))
    p.close()
    p.join()