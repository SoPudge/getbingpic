# -*- coding: utf-8 -*-
import requests
import json
import re

class bing(object):
    def __init__(self):
        pass

    def getpic(self,ds=0):
        urls = []
        [urls.append('https://bing.ioliu.cn/v1/?d=%s&type=json' % d) for d in range(ds)]
        re_pname = re.compile(r'(/rb/)\w{0,10}')
            
        r = requests.get(urls[4])
        pcontent = json.loads(r.content)
        pdate = pcontent['data']['enddate']
        pname = pcontent['data']['url']
        print(type(pname))
        print(re_pname.match(pname).groups())
        #with open('%s.jpg' % d,'wb') as file:
        #   file.write(r.content)

if __name__ == '__main__':
    pic = bing()
    pic.getpic(6)



