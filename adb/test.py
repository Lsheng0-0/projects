# -*- coding: UTF-8 -*-
import os

from adb.dingtalk_api import connect_api, ding_current_api, open_app_api, do_answer_api, connect_status_api, \
    do_checkself_api, refiinsclick_image, start_picdata

# #- 返回键
# re  = os.popen('adb shell input keyevent 4')
# #返回home键（置应用于后台）
# re  = os.popen('adb shell input keyevent 3')
# Lshengpackage.simulate.adb.Command_adb.command().kill()
# print(str(Lshengpackage.simulate.adb.Command_adb.command().dev()))

path = ''
_system = 'adb'
fol_path = path + 'dingding.png'


def first_start():
    con = connect_status_api()
    if con is False:
        connect_api('127.0.0.1:58526')
    elif con is None:
        print('重启app')
        pass
    else:
        print('继续')
        pass
    ding_current_api(fol_path, path, _system)

    refiinsclick_image(fol_path, path, 'is_read', _system)
    open_app_api(fol_path, path, _system, 'op_answer')
    do_answer_api(fol_path, path, _system)

    ding_current_api(fol_path, path, _system)
    open_app_api(fol_path, path, _system, 'op_exaself')
    do_checkself_api(fol_path, path, _system)


start_picdata('image_data.py')
first_start()
# print(lo)
# # re  = os.popen('adb shell uiautomator dump /sdcard/ui.xml') #获得屏幕控件信息
# re = os.popen(r'adb pull /sdcard/ui.xml {}+ui.xml'.format(path))  # 获得屏幕控件信息
