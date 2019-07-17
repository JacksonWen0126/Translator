#/usr/bin/env python
#coding=utf8
 
import http.client
import hashlib
import urllib
import random
import json

appid = '20190717000318689'
secretKey = 'NxxzLemdsPbLBtT2gTGp'

print("""Info: Translate to Chinese : zh
                            English : en
                            Japanese: jp
                            Korean  : kor
                            French  : fra
                            Spanish : spa
                            Thai    : th
                            Arabic  : ara
                            Russian : ru
                            German  : de
                            default : zh""")

httpClient = None
myurl = '/api/trans/vip/translate'
toLang = input("Language : ")
fromLang = 'auto'
q = (input("Enter text : ")).lower()
l = ["zh","en","jp","kor","fra","spa","th","ara","ru","de"]
boo = False
for x in l:
    if toLang == x:
        boo = True
        break

if boo == False:
    toLang ="zh"
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
m1 = hashlib.md5(sign.encode())
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
    response = httpClient.getresponse()
    obc = response.read()
    obc = json.loads(obc)
    obc = obc["trans_result"][0]
    src = obc["src"]
    dst = obc["dst"]
    print("%s translate to %s is %s" %(q,toLang,dst) )



except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()

