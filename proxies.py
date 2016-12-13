# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:55:45 2016

@author: Administrator
"""

import requests
import time
from sendmail import sendmail
import re
from qindao_115_proxy import qiandao_115

def proxy_test(proxy):

    try:
        proxies = {
            "http": "http://" + proxy
            }
        
        #115.com
        time1_1 =time.time()
        requests.get('http://115.com/',proxies = proxies,timeout=3)
        time_num_1 = round(time.time()-time1_1,2)
        
        time.sleep(1)
        
        time1_2 =time.time()
        requests.get('http://web.api.115.com/',proxies = proxies,timeout=3)
        time_num_2 = round(time.time()-time1_2,2)
        
        time_num = max(time_num_1,time_num_2)
        print(proxy,time_num,time_num_1,time_num_2)
        return time_num
#        print(round(time.time()-time1,2))
#        return True
    except Exception as err:  
#        print(err)
        print(proxy,100)
        return 100

def GetFreeProxy():
    url='http://www.xicidaili.com/'
    
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,ja;q=0.6,zh-TW;q=0.4',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        #'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWM5YTVhNjRlMWUxOTBmMjE5YjAwMTcyMThhZjVhMzNjBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWQ5U1prZnI2STlvaFNjSTJGWWhIY3plSjJwSE1RcmR5cGhSMTRwWEwwVms9BjsARg%3D%3D--dbcb01484e42bf27370a95981cd0816f159f4cdc; CNZZDATA1256960793=2050646945-1480229717-null%7C1480777959',
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
    #phone_num=['15694514212','15694638554','15694639084','15698821731','18640815','15942888','15694636714']
        
    phone_num=['18640815','15942888']
    match = GetFreeProxy()
    str_result = '115_qiandao_start...<br>'
    
    if match:

        #签到2次
        for i in range(2):
            #全部完成退出
            if len(phone_num)==0:
                break;
            
            time.sleep(i*5)
            #Log出力
            print('qiandao_num',i+1)
            str_result += str(i+1) + ' ************<br>'
            #标记签到完成的账号用
            phone_num_temp = []
            
            for temp in phone_num:
                print(temp)
                #标记使用过的proxy用
                match_temp = []
                
                for proxy in match:
                    #标记使用过的proxy
                    match_temp.append(proxy)
                    
                    #代理IP可用时（响应<1s），进行签到
                    if (proxy_test(proxy[0]+":"+proxy[1]) < 1):

                        str_result += temp + '>>>' + proxy[0]+":"+proxy[1] + '<br>'
                        try:
                            str_result += qiandao_115(temp,proxy[0]+":"+proxy[1])
                            str_result += '------------<br>'
                            #标记签到完成的账号
                            phone_num_temp.append(temp)
                        except Exception as err: 
                            
                            print(err)
                            str_result += str(err) + '<br>'
                            str_result += '------------<br>'

                        break
                #删除使用完的proxy
                for mm in match_temp:
                    match.remove(mm)
            #删除使用完的账号
            for pp in phone_num_temp:
                phone_num.remove(pp)

    sendmail('115_qiandao_' + time.strftime('%Y-%m-%d'), str_result)
    
if __name__ == '__main__':
    qiandao_115_proxy()
