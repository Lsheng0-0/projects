import os
import pickle
from collections import defaultdict

from PIL import Image


# 转换文件夹下的jpg或者png图片文件为py文件
def pic_to_py(folpath,pypath):
    # 需要转换的图片目录
    image_dir = folpath

    # 遍历目录，将每张图片转换为像素数据
    image_data = defaultdict(list)
    for filename in os.listdir(image_dir):
        # 只处理jpg和png格式的图片
        if filename.endswith('.jpg') or filename.endswith('.png'):
            filepath = os.path.join(image_dir, filename)
            with Image.open(filepath) as img:
                width, height = img.size
                # 获取所有像素的RGB值
                pixel_values = list(img.getdata())
                print(filename.split('.')[0])
                image_data[filename.split('.')[0]].append(
                    {'width': width, 'height': height, 'pixel_values': pixel_values})

    # 将像素数据保存到Python数据文件
    with open(pypath, 'wb') as f:
        pickle.dump(image_data, f)


pic_to_py(folpath = 'adb/pic/dingding',pypath= 'adb/image_data.py')