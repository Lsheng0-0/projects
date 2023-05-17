# 在其他项目中导入Python数据文件
import os
import pickle
from PIL import Image

from adb.dingtalk_api import connect_status_api, connect_api

with open('adb/image_data.py', 'rb') as f:
    image_data = pickle.load(f)

# 显示第一张图像
img_data = image_data['work'][0]
img = Image.new(mode='RGB', size=(img_data['width'], img_data['height']))
img.putdata(img_data['pixel_values'])
img.save('public.png')


_system = 'adb'
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
from Lshengpackage.tools.Loading import load_click, load, insclick
load_click('dingding.png', 'public.png', _system)