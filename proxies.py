# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:55:45 2016

@author: Administrator
"""

import requests
import time
#from sendmail import sendmail
import re
from qindao_115_proxy import qiandao_115

def proxy_test(proxy):

    try:
        proxies = {
            "http": "http://" + proxy
            }
        time1 =time.time()
        requests.get('http://m.115.com',proxies = proxies,timeout=3)
        time_num = round(time.time()-time1,2)
        print(proxy,time_num)
        return time_num
#        print(round(time.time()-time1,2))
#        return True
    except Exception as err:  
#        print(err)
        return 100

def GetFreeProxy():
    url='http://www.xicidaili.com/'
    
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,ja;q=0.6,zh-TW;q=0.4',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWM5YTVhNjRlMWUxOTBmMjE5YjAwMTcyMThhZjVhMzNjBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWQ5U1prZnI2STlvaFNjSTJGWWhIY3plSjJwSE1RcmR5cGhSMTRwWEwwVms9BjsARg%3D%3D--dbcb01484e42bf27370a95981cd0816f159f4cdc; CNZZDATA1256960793=2050646945-1480229717-null%7C1480777959',
        'Host':'www.xicidaili.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    }
    
    text = requests.get(url,headers=headers)
    
    # 将正则表达式编译成Pattern对象
    pattern = re.compile('<td>([0-9\.]+)</td>[^\n]*\n[^<]*<td>([0-9]+)</td>')

    match = pattern.findall(text.text)
    return match

def qiandao_115_proxy():
    phone_num=['15694514212','15694638554','15694639084','15698821731']
#    phone_num=['15694638554','15694639084']
    match = GetFreeProxy()
    if match:
        for temp in phone_num:
            print(temp)
            for proxy in match:
                match.remove(proxy)
                #代理IP可用时（响应<1.2s），进行签到
                if (proxy_test(proxy[0]+":"+proxy[1]) < 1.2):
                    
                    try:
                        qiandao_115(temp,proxy[0]+":"+proxy[1])
                    except Exception as err:  
                        print(err)
                    
                    break