# -*- coding: UTF-8 -*-
import os


# 连接adb
def connect_api(ip):
    connect = os.system('adb connect {}'.format(ip))
    if connect == 0:
        txt = '连接设备{},成功'.format(ip)
        print(txt)
        return txt

# 检测app是否打开
# def exa_app_api():
