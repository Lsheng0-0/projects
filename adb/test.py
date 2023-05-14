# -*- coding: UTF-8 -*-
import os
import sys

import Lshengpackage.simulate.adb.Command_adb
from Lshengpackage.simulate.mock_findPic import find_image
from adb.dingtalk_api import connect_api

# from Lshengpackage.simulate.adb import Pac_adb
# re  = os.system('adb connect 127.0.0.1:58526')
# print(re)

# #- 返回键
# re  = os.popen('adb shell input keyevent 4')
# #返回home键（置应用于后台）
# re  = os.popen('adb shell input keyevent 3')
# Lshengpackage.simulate.adb.Command_adb.command().star()
# Lshengpackage.simulate.adb.Command_adb.command().kill()
# print(Lshengpackage.simulate.adb.Command_adb.command().dev())


fol_path = os.path.dirname(os.path.realpath(__file__)) + '\\pic\\'+'dingding.png'
target_path = os.path.dirname(os.path.realpath(__file__)) + '\\pic\\'+'my.png'
# # connect('127.0.0.1:58526')
find_image(fol_path, target_path,_system='adb')
