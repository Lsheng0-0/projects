# -*- coding: UTF-8 -*-
import logging
import os
import traceback
from time import sleep

import Lshengpackage.Entry
import win32gui
from Lshengpackage import find_image
from mock import tiTget_hwnd, getSpecifiedHwnd, hW_lClick, screenHwnd, screenTopHwnd, getChildHwnd, \
    hide_Hwnd, show_Hwnd, Top_loading, hW_press, back_loading


# 钉钉初始化
def initialization():
    os.startfile('钉钉.lnk')


def 确认组织机构():
    # 截图核对组织是否对
    screenHwnd(jobHwnd)
    organiz = find_image("target/organiz.png")
    print('organiz:' + (str(organiz)))
    if organiz is not None:
        pass
    else:
        # 找到下拉菜单
        down = find_image("target/down.png")
        print('down:' + str(down))
        hW_lClick(int(down[0]), int(down[1]), jobHwnd)  # 下拉菜单
        sleep(0.1)
        # 切换组织
        organizHwnd = win32gui.FindWindow('OrgListSwitcher', None)  # 获取组织句柄
        screenHwnd(organizHwnd)
        organiztion = find_image("target/organiztion.png")
        hW_lClick(int(organiztion[0]), int(organiztion[1]), organizHwnd)
        sleep(0.1)
        PopupFrame = win32gui.FindWindow('PopupFrame', None)  # 获取弹窗句柄
        print('PopupFrame:' + str(PopupFrame))
        hW_lClick(310, 134, PopupFrame)  # 刷新
        sleep(0.5)


def 关闭所有工作台():
    while True:
        print(getChildHwnd('钉钉'))
        new_jobWinHwnd = getChildHwnd('钉钉')[-10]  # 当前窗口倒数第十个
        print('new_jobWinHwnd:' + str(new_jobWinHwnd))
        try:
            screenTopHwnd(dingHwnd, new_jobWinHwnd)  # 工作台当前接口截图
            answer = find_image("target/answer.png")
            print('answer:' + str(answer))
            sleep(0.5)
            show_Hwnd(dingHwnd)
            hW_lClick(int(answer[0]), int(answer[1]), new_jobWinHwnd)
            sleep(0.5)
            new_jobWinHwnd = getChildHwnd('钉钉')[-10]  # 当前窗口倒数第十个
            print('new_jobWinHwnd:' + str(new_jobWinHwnd))
            today = Top_loading(dingHwnd, new_jobWinHwnd, 'todayanswer')
            print('todayanswer：' + str(today))
            if today is not None:
                sleep(0.1)
                show_Hwnd(dingHwnd)
                hW_lClick(int(today[0]), int(today[1]), new_jobWinHwnd)
                break
            else:
                sleep(1)
        except:
            screenHwnd(jobHwnd)
            close_new_jobWinHwnd = find_image("target/close_new_jobWinHwnd.png")
            print('close_new_jobWinHwnd:' + str(close_new_jobWinHwnd))
            if close_new_jobWinHwnd is not None:
                hW_lClick(int(close_new_jobWinHwnd[0]), int(close_new_jobWinHwnd[1]), jobHwnd)  # 关闭现有窗口，直到找到安全答题
            else:
                hW_lClick(100, 100, new_jobWinHwnd)  # 关闭现有窗口，直到找到安全答题
                sleep(0.1)
                hW_press("next")
            sleep(0.5)


def 题目():
    new_jobWinHwnd = getChildHwnd('钉钉')[-10]  # 当前窗口倒数第十个
    sleep(0.2)
    hW_press("next")
    one = Top_loading(dingHwnd, new_jobWinHwnd, '1')
    print('one：' + str(one))
    show_Hwnd(dingHwnd)
    sleep(0.1)
    hW_lClick(int(one[0]), int(one[1]), new_jobWinHwnd)  # 打开题目
    sleep(0.1)
    hW_lClick(int(one[0]), int(one[1]), new_jobWinHwnd)  # 打开题目


def 选项():
    new_jobWinHwnd = getChildHwnd('钉钉')[-10]  # 当前窗口倒数第十个
    select = Top_loading(dingHwnd, new_jobWinHwnd, 'select')
    print('select:' + str(select))
    y = 0
    for i in range(4):
        show_Hwnd(dingHwnd)
        sleep(0.1)
        hW_lClick(int(select[0]), int(select[1]), new_jobWinHwnd)  # 打开选项
        sleep(0.1)
        hW_lClick(int(select[0]), int(select[1]) + 70 + y, new_jobWinHwnd)  # 遍历A、B、C、D
        screenTopHwnd(dingHwnd, new_jobWinHwnd)
        yesok = find_image("target/yesok.png")
        if yesok is not None:
            print('yesok:' + str(yesok))
            break
        sleep(0.5)
        y = y + 33


def 刷题():
    new_jobWinHwnd = getChildHwnd('钉钉')[-10]  # 当前窗口倒数第十个
    
    选项()
    for i in range(4):
        screenTopHwnd(dingHwnd, new_jobWinHwnd)
        next = find_image("target/next.png")
        print('next:' + str(next))
        show_Hwnd(dingHwnd)
        sleep(0.1)
        hW_lClick(int(next[0]), int(next[1]), new_jobWinHwnd)  # 打开选项
        选项()
    screenTopHwnd(dingHwnd, new_jobWinHwnd)
    green_over = find_image("target/green_over.png")
    print('green_over:' + str(green_over))
    show_Hwnd(dingHwnd)
    sleep(0.1)
    hW_lClick(int(green_over[0]), int(green_over[1]), new_jobWinHwnd)  # 点击完成
    sleep(0.1)
    screenTopHwnd(dingHwnd, new_jobWinHwnd)
    green_up = find_image("target/green_up.png")
    print('green_up:' + str(green_up))
    show_Hwnd(dingHwnd)
    sleep(0.1)
    hW_lClick(int(green_up[0]), int(green_up[1]), new_jobWinHwnd)  # 点击提交


自查翻页 = ['next', 'prior']


def 自查():
    screenHwnd(jobHwnd)
    isnotwork = find_image("target/isnotwork.png")
    print('isnotwork:' + str(isnotwork))
    if isnotwork is not None:
        hW_lClick(int(isnotwork[0]), int(isnotwork[1]), jobHwnd)  # 办公
        sleep(0.1)
    bangong_jobWinHwnd = getChildHwnd('钉钉')[-13]  # 当前窗口倒数第十3个
    print('bangong_jobWinHwnd:' + str(bangong_jobWinHwnd))
    sleep(0.1)
    page = 0
    while True:
        screenTopHwnd(dingHwnd, bangong_jobWinHwnd)
        examine = find_image("target/examine.png")
        print('examine:' + str(examine))
        if examine is None:
            sleep(0.1)
            show_Hwnd(dingHwnd)
            sleep(0.3)
            hW_lClick(198, 376, bangong_jobWinHwnd)
            sleep(0.3)
            if page << 3:
                print(自查翻页[0])
                hW_press(自查翻页[0])
            else:
                hW_press(自查翻页[1])
            page = +1
            sleep(0.5)
        else:
            show_Hwnd(dingHwnd)
            hW_lClick(int(examine[0]), int(examine[1]), bangong_jobWinHwnd)  # 办公
            break


def mock_loading(mianHwnd, childrenHwnd, target):
    # 直到找到点击，底层
    tar = Top_loading(mianHwnd, childrenHwnd, target)
    print(tar)
    show_Hwnd(dingHwnd)
    sleep(0.1)
    hW_lClick(int(tar[0]), int(tar[1]), childrenHwnd)
    sleep(0.2)
    
def 三下走(mianHwnd, childrenHwnd, target):
    ti = 0
    while True:
        if ti == 3:
            return False
        else:
            screenTopHwnd(mianHwnd, childrenHwnd)  # 工作台当前接口截图
            tar = find_image("target/{}.png".format(target))
            print(tar)
            if tar is not None:
                sleep(0.1)
                show_Hwnd(dingHwnd)
                sleep(0.1)
                hW_lClick(int(tar[0]), int(tar[1]), childrenHwnd)
                return True
            else:
                sleep(0.2)
            ti +=1
def 填写内容():
    lowHwnd = getChildHwnd('钉钉')[-10]  # 当前窗口倒数第十个
    mock_loading(dingHwnd, lowHwnd, target='city')
    mock_loading(dingHwnd, lowHwnd, target='jiujiang')
    mock_loading(dingHwnd, lowHwnd, target='region')
    mock_loading(dingHwnd, lowHwnd, target='lianxiqu')
    mock_loading(dingHwnd, lowHwnd, target='lines')
    mock_loading(dingHwnd, lowHwnd, target='weihu')
    hW_press('next')
    mock_loading(dingHwnd, lowHwnd, target='zhuanye')
    mock_loading(dingHwnd, lowHwnd, target='jike')
    wendu = 三下走(dingHwnd, lowHwnd, target='wendu' )
    if wendu is False:
        三下走(dingHwnd, lowHwnd, target='wendu2')
    else:
        pass
    Lshengpackage.Entry.insert('36')
    三下走(dingHwnd, lowHwnd, 'yes_')
    三下走(dingHwnd, lowHwnd, 'yes_')
    三下走(dingHwnd, lowHwnd, 'yes_')
    show_Hwnd(dingHwnd)

    sleep(0.1)
    hW_lClick(200,200, lowHwnd)
    hW_press('next')

    三下走(dingHwnd, lowHwnd, 'yes_')
    三下走(dingHwnd, lowHwnd, 'yes_')
    三下走(dingHwnd, lowHwnd, 'yes_')
    show_Hwnd(dingHwnd)

    sleep(0.1)
    hW_lClick(200, 200, lowHwnd)
    hW_press('next')
    三下走(dingHwnd, lowHwnd, 'yes_')
    三下走(dingHwnd, lowHwnd, 'yes_')
    三下走(dingHwnd, lowHwnd, 'yes_')
    三下走(dingHwnd, lowHwnd, 'yes_')
    show_Hwnd(dingHwnd)

    sleep(0.1)
    hW_lClick(200, 200, lowHwnd)
    hW_press('next')
    三下走(dingHwnd, lowHwnd, 'yes_')
    三下走(dingHwnd, lowHwnd, 'yes_')
    三下走(dingHwnd, lowHwnd, 'yes_')
    mock_loading(dingHwnd, lowHwnd, 'green_up')

def open_dingding():
    initialization()
    tar = back_loading('钉钉', 'logo')
    return tar

if __name__ == '__main__':
    while True:
        try:
            tar = open_dingding()
            if tar is not None:
                print(tar)
                break
            else:
                sleep(1)
        except:
            print('报错')
            sleep(1)
    

    # 获取 钉钉 句柄
    dingHwnd = tiTget_hwnd('钉钉')
    print('dingHwnd:' + (str(dingHwnd)))
    # 获得侧边栏句柄
    sidebarHwnd = getSpecifiedHwnd(dingHwnd, 'Navigator', '')[0]  # 侧边栏
    print('sidebarHwnd:' + (str(sidebarHwnd)))
    # 后台点击工作台
    hW_lClick(32, 136, sidebarHwnd)
    # 获取工作台句柄
    jobHwnd = getSpecifiedHwnd(dingHwnd, 'StandardFrame_WorkWnd', '工作')[0]  # 工作台
    print('jobHwnd:' + (str(jobHwnd)))
    while True:
        # 引入日志
        logging.basicConfig(
            filename='log_record.txt',
            level=logging.DEBUG, filemode='w', format='[%(asctime)s] [%(levelname)s] >>>  %(message)s',
            datefmt='%Y-%m-%d %I:%M:%S'
            )
    
        try:
            确认组织机构()
            关闭所有工作台()
            题目()
            刷题()
            自查()  # 5512978
            填写内容()
            break
        except Exception as e:
            logging.error("Main program error:")
            logging.error(e)
            logging.error(traceback.format_exc())
