# -*- coding: utf-8 -*-
import requests
import json
import re

class bing(object):
    def __init__(self):
        pass

    def getpic(self,ds=0):
        #urls是存储io壁纸网站每日壁纸地址的列表
        #壁纸地址是json内容，为了方便后面通过正则去掉json返回值，所以加上了分辨率
        #两个正则一个是获取壁纸地址当中的bing网站地址中的壁纸名称，另一个是获取不带json的url，方便下载抓取，因为bing的地址经常无壁纸存在
        urls = []
        [urls.append('https://bing.ioliu.cn/v1/?d=%s&w=1920&h=1080&type=json' % d) for d in range(ds)]
        re_pname = re.compile(r'(.*)rb/(.*?)(_.*)')
        re_piourl = re.compile(r'(.*)&type=json')
            
        #循环获取status状态，为-1则说明该日无壁纸抓取
        for n in range(ds):
            r = requests.get(urls[n])
            pcontent = json.loads(r.content)
            piostatu = pcontent['status']['code']
            if piostatu == -1:
                print('%s/%s|no pic' % (n,ds))
                continue
            else:
                pdate = pcontent['data']['enddate']
                pbingurl = pcontent['data']['url']
                pname = re_pname.match(pbingurl).group(2) 
                piourl = re_piourl.match(urls[n]).group(1)
                pic = requests.get(piourl)
                with open('%s.jpg' % pname,'wb') as file:
                    file.write(pic.content)
                print('%s/%s|get the %s pic,name is %s' % (n,ds,pdate,pname))
        print('done')
             

if __name__ == '__main__':
    pic = bing()
    pic.getpic(365)



