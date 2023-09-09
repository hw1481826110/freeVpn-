import requests
import os
print("账号"+os.environ.get('user')+" 密码："+os.environ.get('password'))
def checkin(Email,passwd):
    import requests
    url="https://go.runba.cyou/auth/login"
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69'
    }
    data={
        "email":Email,
        "passwd":passwd
    }
    resp=requests.post(url,headers=headers,data=data)
    to_set_cookie = requests.utils.dict_from_cookiejar(resp.cookies)
    if not (resp.status_code==200 and resp.json().get('ret')==1):
        print("登陆失败",resp.text)
        exit(0)
    else:
        print('用户==>',to_set_cookie.get('email'),'登陆成功')
    checkin_url="https://go.runba.cyou/user/checkin"
    resp2=requests.post(checkin_url,headers=headers,cookies=to_set_cookie)
    if resp2.status_code==200:
        if resp2.json().get("ret")==1:
            print("*"*10+"签到成功"+10*"*")
            print("签到获得流量==>",resp2.json().get('msg'))
            print("剩余流量==>",resp2.json().get('trafficInfo').get('unUsedTraffic'))
            print("已经使用==>",resp2.json().get('trafficInfo').get('lastUsedTraffic'))
            print("今日使用==>",resp2.json().get('trafficInfo').get('todayUsedTraffic'))
            pushplus("vpnfree签到成功","剩余流量==>"+resp2.json().get('trafficInfo').get('unUsedTraffic')+"/n")
        else:
            print(resp2.json().get("msg"))
            pushplus("vpnfree签到失败",resp2.json().get("msg"))
    return resp2
def pushplus( title, content):
    content = content.replace("\n", "\n\n")
    payload = {
        'token': "3adb410539df4a9c8fe5d6c37f4edec8",
        "title": title,
        "content": content,
        "channel": "wechat",
        "template": "markdown"
    }
    resp = requests.post("http://www.pushplus.plus/send", data=payload)
    resp_json = resp.json()
    if resp_json["code"] == 200:
        print(f"[Pushplus]Send message to Pushplus successfully.")
    if resp_json["code"] != 200:
        print(f"[Pushplus][Send Message Response]{resp.text}")
        return -1
    return 0
checkin(os.environ.get('user'),os.environ.get('password'))


