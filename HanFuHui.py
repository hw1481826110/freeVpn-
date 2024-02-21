#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ast import main
from multiprocessing.spawn import _main
from re import L
import requests
import json

def qiandao(token):
    if token is not None:
        print("token")
    else:
        print("token为空")
    print(token)
    url = 'https://api5.hanfuhui.com/Hanbi/InsertSignin'
    headers = {
    'Host': 'api5.hanfuhui.com',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'sec-ch-ua': '"Android WebView";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'hanfuhui_app': 'hanfuhui',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; KB2000 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.193 Mobile Safari/537.36hui_android',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'hanfuhui_fromclient': 'h5',
    'hanfuhui_token': token,
    'sec-ch-ua-platform': '"Android"',
    'Origin': 'https://www.hanfuhui.com',
    'X-Requested-With': 'com.hanfuhui',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.hanfuhui.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
    }
    #  'hanfuhui_signature': 'NiFVtkpgXYCgEvoeTCu5f0zrxmg1YJuNdBK3uu0+kazcuOXGavrji4SR9oAB8Fq5FHPdOIF72iLyWhQBD6FknO+AZLBysHH0eq04+gMD7R+LKF3HOl7rde2+DNGtzcslJJwzMl0LlPxinGY/wMfPnD2ECMxKbwR38j0jDkbS9mY=',
    cookies = {}
    data = {}
    

    html = requests.post(url, headers=headers,  cookies=cookies, data=json.dumps(data))
    print(html.text)

def res_code(str): # 获取res加密数据
    #html = requests.post("https://www.hanfuhui.com/Home/Rsa?text=" +, ,  , data=json.dumps(data))
    html = requests.get("https://www.hanfuhui.com/Home/Rsa?text=" +str)
    print(html.text)
    return (html.text)

def gettoken():
    url = "https://www.hanfuhui.com/Api/GetAppToken"

    
    payload = ""
    headers = {
    
    "Host": "www.hanfuhui.com",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Referer": "https://www.hanfuhui.com/Account?from=http%253a%252f%252fwww.hanfuhui.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    print(response.text)
    return (response.text)
def login(user,password):

    url = "https://api5.hanfuhui.com/Account/LoginForPhone"
    userOrName=res_code(user+","+password)
    payload = "usersecret="+userOrName+"&phonecountry=86"
    headers = {
    "Host": "api5.hanfuhui.com",
    "Connection": "keep-alive",
    "Content-Length": "213",
    "hanfuhui_app": "hanfuhui",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "hanfuhui_fromclient": "PC",
    "hanfuhui_token": "null",

     "hanfuhui_signature": gettoken(),
    "Origin": "https://www.hanfuhui.com",
    "Referer": "https://www.hanfuhui.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    if(response.status_code==200):
        print("sueeses")
        a=json.loads(response.text)
        AccessTokenken=a.get("Data", {}).get("AccessToken")
        return AccessTokenken
    
    else:
        print("false")
    return AccessTokenken
    
if __name__ == '__main__':
    #token=
    qiandao(login("13145487071","hw1481826110"))





    
    