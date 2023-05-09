# -*- coding: UTF-8 -*-
import os
from time import sleep
import win32ui
from Lshengpackage import find_image
from PIL import Image
from PyQt5.QtWidgets import QApplication
import sys
import win32api
import win32con
import win32gui

keycodes = {
    "BACK": 0x08,
    "TAB": 0x09,
    "RETURN": 0x0D,
    "ESCAPE": 0x1B,
    "SPACE": 0x20,
    "PRIOR": 0x21,
    "NEXT": 0x22,
    "END": 0x23,
    "HOME": 0x24,
    "LEFT": 0x25,
    "UP": 0x26,
    "RIGHT": 0x27,
    "DOWN": 0x28,
    "PRINT": 0x2C,
    "INSERT": 0x2D,
    "DELETE": 0x2E,
    "back": 0x08,
    "tab": 0x09,
    "return": 0x0D,
    "escape": 0x1B,
    "space": 0x20,
    "prior": 0x21,
    "next": 0x22,
    "end": 0x23,
    "home": 0x24,
    "left": 0x25,
    "up": 0x26,
    "right": 0x27,
    "down": 0x28,
    "print": 0x2C,
    "insert": 0x2D,
    "delete": 0x2E,
    "0": 0x30,
    "1": 0x31,
    "2": 0x32,
    "3": 0x33,
    "4": 0x34,
    "5": 0x35,
    "6": 0x36,
    "7": 0x37,
    "8": 0x38,
    "9": 0x39,
    "A": 0x41,
    "B": 0x42,
    "C": 0x43,
    "D": 0x44,
    "E": 0x45,
    "F": 0x46,
    "G": 0x47,
    "H": 0x48,
    "I": 0x49,
    "J": 0x4A,
    "K": 0x4B,
    "L": 0x4C,
    "M": 0x4D,
    "N": 0x4E,
    "O": 0x4F,
    "P": 0x50,
    "Q": 0x51,
    "R": 0x52,
    "S": 0x53,
    "T": 0x54,
    "U": 0x55,
    "V": 0x56,
    "W": 0x57,
    "X": 0x58,
    "Y": 0x59,
    "Z": 0x5A,
    "a": 0x61,
    "b": 0x62,
    "c": 0x63,
    "d": 0x64,
    "e": 0x65,
    "f": 0x66,
    "g": 0x67,
    "h": 0x68,
    "i": 0x69,
    "j": 0x6A,
    "k": 0x6B,
    "l": 0x6C,
    "m": 0x6D,
    "n": 0x6E,
    "o": 0x6F,
    "p": 0x70,
    "q": 0x71,
    "r": 0x72,
    "s": 0x73,
    "t": 0x74,
    "u": 0x75,
    "v": 0x76,
    "w": 0x77,
    "x": 0x78,
    "y": 0x79,
    "z": 0x7A,
    "NUM0": 0x60,
    "NUM1": 0x61,
    "NUM2": 0x62,
    "NUM3": 0x63,
    "NUM4": 0x64,
    "NUM5": 0x65,
    "NUM6": 0x66,
    "NUM7": 0x67,
    "NUM8": 0x68,
    "NUM9": 0x69,
    "num0": 0x60,
    "num1": 0x61,
    "num2": 0x62,
    "num3": 0x63,
    "num4": 0x64,
    "num5": 0x65,
    "num6": 0x66,
    "num7": 0x67,
    "num8": 0x68,
    "num9": 0x69,
    "F1":  0x70,
    "F2":  0x71,
    "F3":  0x72,
    "F4":  0x73,
    "F5":  0x74,
    "F6":  0x75,
    "F7":  0x76,
    "F8":  0x77,
    "F9":  0x78,
    "F10": 0x79,
    "F11": 0x7A,
    "F12": 0x7B,
    "NUMLOCK": 0x90,
    "f1":  0x3A,
    "f2":  0x3B,
    "f3":  0x3C,
    "f4":  0x3D,
    "f5":  0x3E,
    "f6":  0x3F,
    "f7":  0x40,
    "f8":  0x41,
    "f9":  0x42,
    "f10": 0x43,
    "f11": 0x44,
    "f12": 0x45,
    "numlock": 0x90
}


all_Hwnd = dict()

def is_folder():
    folder = os.path.join(os.path.dirname(__file__), ) + "\\pic"
    # 判断是否有pic文件夹
    if not os.path.exists(folder):
        os.mkdir(folder)

def Top_hwnd():
    # 获取当前窗口
    return win32gui.GetForegroundWindow()

def toTop_hwnd(hwnd):
    # 指定窗口放到最顶端
    win32gui.SetForegroundWindow(hwnd)
    sleep(0.1)

def show_Hwnd(top_hwnd):
    if top_hwnd != 0:
        # 激活窗口
        if win32gui.IsIconic(top_hwnd):
            win32gui.ShowWindow(top_hwnd, win32con.SW_SHOWNORMAL)  # 显示
            sleep(0.1)
        else:
            toTop_hwnd(top_hwnd)

def hide_Hwnd(hwnd):
    # 影藏窗口
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWMINIMIZED)
    sleep(0.1)

def findHwnd(clsname, title):
    # 从顶层窗口向下搜索主窗口，无法搜索子窗口
    # FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名
    Hwnd = win32gui.FindWindow(clsname, title)
    return Hwnd


def get_allHwnd(hwnd, mouse):
    # 字典启动的所有窗口
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        all_Hwnd.update({hwnd: win32gui.GetWindowText(hwnd)})


def tiTget_hwnd(title):
    # 遍历出title的hwnd
    win32gui.EnumWindows(get_allHwnd, None)
    # print(all_Hwnd.items())
    for h, t in all_Hwnd.items():
        if t == title:
            return h


def getSpecifiedHwnd(hwnd, clsname=None, title=None):
    """
    :param hwnd: 父窗口句柄
    :param title: 指定子窗口名
    :param clsname: 指定子窗口类名
    :return: 返回父窗口下所有子窗体的句柄
    """
    windows = []
    hwndChild = win32gui.FindWindowEx(hwnd, None, clsname, title)
    windows.append(hwndChild)
    while True:
        hwndChild = win32gui.FindWindowEx(hwnd, hwndChild, clsname, title)
        if hwndChild:
            windows.append(hwndChild)
        else:
            return windows


def getChildHwnd(title):
    # 获取子hwnd
    # print(tiTget_hwnd(title))
    hWnd_child_list = []
    win32gui.EnumChildWindows(tiTget_hwnd(title), lambda hwnd, param: param.append(hwnd), hWnd_child_list)
    return hWnd_child_list


def screenHwnd(title):
    sleep(0.1)
    # 判断是否有pic文件夹
    is_folder()
    # 窗口截图,可遮挡,需保证窗口不最小化
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    if type(title) is str:
        if tiTget_hwnd(title) is not None:
            img = screen.grabWindow(tiTget_hwnd(title)).toImage()
            img.save(os.path.join(os.path.dirname(__file__), ) + "\\pic\\screen.png")
        else:
            print('无窗口')
    else:
        img = screen.grabWindow(title).toImage()
        img.save(os.path.join(os.path.dirname(__file__), ) + "\\pic\\screen.png")


def screenTopHwnd(top_hwnd, child_hwnd):
    # 判断是否有pic文件夹
    is_folder()
    # 子窗口截图 Hwnd (因对截图黑白屏)
    show_Hwnd(top_hwnd)
    left, top, right, bot = win32gui.GetWindowRect(child_hwnd)
    w = right - left
    h = bot - top
    # 窗口置顶
    win32gui.SetForegroundWindow(top_hwnd)
    sleep(0.3)
    # 获取桌面窗口
    hdesktop = win32gui.GetDesktopWindow()
    # 获取窗口 DC
    hwndDC = win32gui.GetWindowDC(hdesktop)
    # 从句柄创建 DC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # 创建兼容 DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建位图
    saveBitMap = win32ui.CreateBitmap()
    # 创建兼容的位图
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    result = saveDC.BitBlt((0, 0), (w, h), mfcDC, (left, top), win32con.SRCCOPY)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer('RGB',(bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    # 最小化窗口
    hide_Hwnd(top_hwnd)
    # 释放内存
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hdesktop, hwndDC)
    if result is None:
        # PrintWindow Succeeded
        im.save(os.path.join(os.path.dirname(__file__), ) + r"\\pic\\screen.png")

def hWget_title(hwnd):
    # 根据句柄查找窗口标题
    return win32gui.GetWindowText(hwnd)

def getHwnd_rect(hwnd):
    # 获取窗口左上角坐标和右下角坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # 输出坐标信息
    print('窗口左上角坐标：({}, {})'.format(left, top))
    print('窗口右下角坐标：({}, {})'.format(right, bottom))

def oF_lClick(x, y, offset):
    # 偏移offset（1.25 = %125）
    x = int(x / offset)
    y = int(y / offset)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def hW_lClick(x, y, hwnd):
    # hwnd为窗口控件的句柄，x,y窗口相对坐标
    long_position = win32api.MAKELONG(x, y)  # 模拟鼠标指针传送到指定坐标
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 发送鼠标按下信号
    sleep(0.1)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 发送鼠标松开信号

def hW_press(keycode):
    win32api.keybd_event(keycodes['{}'.format(keycode)], 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    win32api.keybd_event(keycodes['{}'.format(keycode)], 0, win32con.KEYEVENTF_KEYUP, 0)

def back_loading(title, target):
    # 后台加载
    while True:
        screenHwnd(title)  # 工作台当前接口截图
        tar = find_image("target/{}.png".format(target))
        if tar is not None:
            return tar
        else:
            sleep(1)
    
def Top_loading(mianHwnd, childrenHwnd, target):
    # 置顶加载
    while True:
        screenTopHwnd(mianHwnd, childrenHwnd)  # 工作台当前接口截图
        sleep(0.1)
        tar = find_image("target/{}.png".format(target))
        if tar is not None:
            sleep(0.1)
            return tar
        else:
            sleep(1)