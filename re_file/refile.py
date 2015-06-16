#coding=utf-8
import re

with open('domains.txt','r') as data:
    data = data.read()

def get_domains_in_text(str_data):
    str_data=str_data.replace(' ','')
    print str_data
    pattern = re.compile('(.*?\.com).*?国.*?理\n+',re.S)
    data = re.findall(pattern,str_data)
    return data

allurls=[]
allurls = get_domains_in_text(data)

with open('domains_results.txt','a') as data:
    for x in allurls:
        if x:
            x = 'http://' + x +'\n'
            data.write(x)
            print 'ok!'