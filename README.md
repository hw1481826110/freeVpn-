# [freeVpn]("https://go.runba.cyou/user")
> 每日自动签到，不需要服务器，直接fork进仓库，然后点击actions，即可每日自动化运行
## 如何使用？ 
1. Fork项目到自己的仓库
2. 点击Settings -> 点击选项卡 Secrets and variables -> 点击Actions -> New repository secret


    | Name   | Secret                           |
    | ------ | ------------------------------- |
    | USER *   | 账号 |
    | PASSWORD *  | 密码 |
    | PUSHPLUS_TOKEN  | pushplus 推送Token |


以上USER、PASSWORD为阿里云盘签到必填项 推送可以选择PUSHPLUS_TOKEN
```
python main.py
```

