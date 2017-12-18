# -*- coding: utf-8 -*-
import requests
import json
import re

class bing(object):
    def __init__(self):
        pass

    def getpic(self,ds=0):
        urls = []
        [urls.append('https://bing.ioliu.cn/v1/?d=%s&w=1920&h=1080&type=json' % d) for d in range(ds)]
        re_pname = re.compile(r'(.*)rb/(.*?)(_.*)')
        re_piourl = re.compile(r'(.*)&type=json')
            
        #for n in range(ds):
        #    r = requests.get(urls[n])
        #    pcontent = json.loads(r.content)
        #    pdate = pcontent['data']['enddate']
        #    pbingurl = pcontent['data']['url']
        #    pname = re_pname.match(pbingurl).group(2) 
        #    piourl = re_piourl.match(urls[n]).group(1)
        #    #print(pdate)
        #    #print(pname)
        #    #print(pbingurl)
        #    #print(urls[n])
        #    #print(piourl)
        #    pic = requests.get(piourl)
        #    with open('%s.jpg' % pname,'wb') as file:
        #        file.write(pic.content)
        #    print('%s/%s|get the %s pic,name is %s' % (n,ds,pdate,pname))
        #print('done')

        n = 95
        r = requests.get(urls[n])
        pcontent = json.loads(r.content)
        pdate = pcontent['data']['enddate']
        pbingurl = pcontent['data']['url']
        pname = re_pname.match(pbingurl).group(2) 
        piourl = re_piourl.match(urls[n]).group(1)
        print(pdate)
        print(pname)
        print(pbingurl)
        print(urls[n])
        print(piourl)
        pic = requests.get(piourl)

if __name__ == '__main__':
    pic = bing()
    pic.getpic(365)



