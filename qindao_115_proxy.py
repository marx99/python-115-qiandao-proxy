# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:55:28 2016

@author: Administrator
"""
import requests
import time
from sendmail import sendmail

#115 qiandao
cookies = {
    'test':'test',
#    '15694514212':'OOFL=592637923; UID=592637923_A1_1480855018; CID=2f595436d8186e2178f2ce4f9189b39b; SEID=c1b751114ff2e3ab2c039cc5c21a19cd39007249ff80132d2c752b0810ac9864fd560c29b2d403b994e2a9832ed0bc07ad71da3efdee386a6f72589d; ssov_592637923=0_592637923_221899932422c0b2d6b806dd32473d73',
    '15694514212':'OOFL=592637923; UID=592637923_A1_1480858207; CID=a27aca28edb1f3d6d9900b98f9d2da34; SEID=1382b4d92f86d3a5a49309c5c3395c5b7f56c314102e85a94fc175588663c115db632d8593e4d57ea1a3729add42bcba521f8569bd4ed0c4cfcb0828; ssov_592637923=0_592637923_221899932422c0b2d6b806dd32473d73',
#    '15694638554':'OOFL=592638123; UID=592638123_A1_1480855159; CID=58ec2bc7184db4f63cb078406748c86f; SEID=f5465bbb3c27d2e9baf974848a7c9c93e15b399dd3385d13ff2b259bcd33cf6907d526b1a07b1f91e5eb2f35bcc0607d5a8ba18e17500b04fd5ecc43; ssov_592638123=0_592638123_80868ab938694b252b118e42069a97ff',
    '15694638554':'OOFL=592638123; UID=592638123_A1_1480858387; CID=ebf04bd84d9c4b824b410ccbd2151a5b; SEID=4e7d12468fe9196f5b6e6314b34b44efe51f3022b13f6bad431bde679ce1c9de13176ad28b2ce8ef8c579599b617db4d48f8ee1776b791fc6f348688; ssov_592638123=0_592638123_80868ab938694b252b118e42069a97ff',
#    '15694639084':'OOFL=592637925; UID=592637925_A1_1480855726; CID=0fe0047353457c21d99925c9d964e752; SEID=7dc72be9280f0f5c4a2760cd3693adb3c6fc39d682c40c0c3de5e64d859d74cde235155ffdfd76754d31094b6e2be773abfc6f4173d88bd989604b5d; ssov_592637925=0_592637925_c4528d13e26d353ce715912f2e10b498',
    '15694639084':'OOFL=592637925; UID=592637925_A1_1480858453; CID=4a6d25c90765e8cab92949ee6743edaa; SEID=210824b20c32baccf61996ba3f2a1db0a055213d884bd0bd4e8d2cf97994e7b0b999d700706adf8e8415e115e37b0121e47966201b7318333564055f; ssov_592637925=0_592637925_c4528d13e26d353ce715912f2e10b498',
    '15698821731':'OOFL=592638124; UID=592638124_A1_1480855800; CID=ba22c5690ee304743fa87270b9fe568a; SEID=817f726b159ec33d60008335234c0bfaa3e54b4fcd7d7110024dae045d534b4cd98a376cd205647f7079ccfdee0325afca959056709d3546099e365f; ssov_592638124=0_592638124_03e508b43caad40f4ad5c3e0d62a1579',
#    '15942888': 'OOFA=UID=4158054_F1_1479007096; UID=4158054_F1_1479007096; CID=9cd9bb99b3101593697536c1b6a0e233; SEID=a94f79f65a4bed45cbff606930239896f115df9d81b7bafae1f34d66b87108123c35ceed4adb846076d9e1024d5c82721e2e62fcea6693104e3378ad; ssov_4158054=0_4158054_e4b7e5bba4f3176fa4343b12dd42aa3b',
    '15942888': 'ssov_4158054=0_4158054_e4b7e5bba4f3176fa4343b12dd42aa3b; OOFL=4158054; UID=4158054_A1_1481384745; CID=02d705094de64b6e7cf47c2c588dbc0e; SEID=a7dbeb121343ffae25dd6783f814dc7b1a289467b252cbf7e4e01e090c1ca81d1707a87649b8a5c8e8860f5c72c167416888ba6c66d65abc35dfe7ae',
    '13555925': 'ssov_590519292=0_590519292_e41cbbf54df9d773385c0492dc79c354; OOFA=SEID=7eb6ba018b0be0e9869af0ed02957d3cc4e96181543d97ab691c2aa195349a0abb650769e034a4b0ea53c142be74ddbbb29104fcc6465c937894a842; SEID=7eb6ba018b0be0e9869af0ed02957d3cc4e96181543d97ab691c2aa195349a0abb650769e034a4b0ea53c142be74ddbbb29104fcc6465c937894a842; UID=590519292_F1_1477144725; CID=3eee667f5650c9315a1961ec7d5efcff',
#    '18640815': 'CID=75a2513cf5f55d0eb20510d701e354ed; SEID=e4bee56b359d5fbe50814a98857617657ffda3200e72e804f66a9a8e22edaf851a000ee6b79bd77e2630fb9c784bfa618700d78d5f4039bfad9ab17f; ssov_592637961=0_592637961_ed7d57ec15b95004e985cae17b31a407; UID=592637961_H1_1478431292',
    '18640815': 'OOFL=592637961; UID=592637961_A1_1481027498; CID=4c3aea3159677ad491991d6fce442c3d; SEID=05ffad2c3f3d0acdbae85c940d8e8daf2d02758aa595c4361422c17d75fa8561cc0aef0ba01b4ebe8c8c1dd8c2fde920d9a5cf99b8d3423b8b429a0e; ssov_592637961=0_592637961_ed7d57ec15b95004e985cae17b31a407',
    #'15694636714': 'CID=d88b040909b38a3d14c7fa78cc6032aa; SEID=354b4a3fc4f04389f3e5e5814e92f5d40e46893a0fcc55865d1de79f21ccb405acd2c1e73b9f311f1476cbeceebef8c5539f3f489923737acb6d2330; ssov_592637924=0_592637924_890a4b2e72593f4e25ee9a16149b45d1; UID=592637924_H1_1478958011'
    '15694636714':'OOFL=592637924; UID=592637924_A1_1481458773; CID=d0fb424e66de950d0ab3ad35339c9d65; SEID=ac689b8b0d3f3b8d6bf2e56ad09be5f071e305f722d9d608c639b3066f61fd57d1f0193ffcff231c562d17ac5c3dc2ff63623044c1a326bf797e1e5e; ssov_592637924=0_592637924_890a4b2e72593f4e25ee9a16149b45d1'
}

def qiandao_115(userid,proxy):
     # 签到
    proxies = {
        "http": "http://" + proxy
    }
    #结果
    str_result = ''
    #login
    sign_headers = {
        'Host': '115.com',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; 2014811 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 115disk/6.2.1',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'Cookie': cookies[userid],
        'X-Requested-With': 'com.ylmf.androidclient'    
    }
    sign_url = 'http://115.com/?ct=sign'
    
    try:
        
        sign_str = requests.get(sign_url,headers = sign_headers,proxies=proxies,timeout=6)
        
        print('sign ' + userid,sign_str.status_code)
        #str_result = 'sign ' + userid + '<br>'
    except Exception as err:  
        str_result = 'sign ' + str(err) + '<br>'
        
    time.sleep(5)
    
    #post
    postheaders = {
        'Host': 'web.api.115.com',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-cn',
        'Accept': '*/*',
        'Origin': 'http://web.api.115.com',
        'Content-Length': '0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; 2014811 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 115disk/6.2.1',
        #'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 UPad/6.2.0',
        'Referer': 'http://web.api.115.com/bridge_2.0.html?namespace=FS.DataSrv&api=UDataAPI&_t=v5',
        'Cookie': cookies[userid]
    }
    
    posturl='http://web.api.115.com/user/sign'
    postr = requests.post(posturl,headers = postheaders,proxies=proxies,timeout=6)
    print( 'post ' + userid,postr.status_code,postr.json())
    str_result += 'post ' + userid + str(postr.json()) + '<br>'
    
    time.sleep(2)
    
    #get result 
    #geturl = 'http://web.api.115.com/user/sign?start=2016-11-01&_=1478610072924'
    geturl = 'http://web.api.115.com/user/sign?start='+ time.strftime('%Y-%m-01') +'&_=' + str(round(time.time()*1000))
    #result output
    
    try:
        
        get_str = requests.get(geturl,headers = postheaders,proxies=proxies,timeout=6)
        print( 'result ' + userid,get_str.status_code,get_str.json())
    
        #str_result += 'result ' + userid + str(get_str.json()) + '<br>'
    except Exception as err:  
        print( 'result ' + userid,str(err))
        str_result += 'result ' + userid + str(err) + '<br>'
        
    return str_result
    #send mail
#    sendmail('115_qiandao_' + userid + '_' + time.strftime('%Y-%m-%d'), str(postr.json()) + '<br>' + str(get_str.json()))
