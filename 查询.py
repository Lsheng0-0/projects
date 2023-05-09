# -*- coding: UTF-8 -*-
# 遍历当前窗口的句柄及标题并输出至控制台
import win32gui

hwnd_title = {}


def get_all_hwnd(hwnd, self):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({win32gui.GetWindowText(hwnd): hwnd})


win32gui.EnumWindows(get_all_hwnd, 0)

for t, h in hwnd_title.items():
    if h:
        print(t + ":" + str(h))
