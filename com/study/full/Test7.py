"""
https://mp.weixin.qq.com/s/UDYNWN5_iFoJd4GT--XyDg
10几行代码，用python打造实时截图识别OCR
"""

import keyboard

# 利用截图软件（Snipaste）截图到剪贴板
# 输入键盘的触发事件
keyboard.wait(hotkey="f1")
keyboard.wait(hotkey="ctrl+c")
# time.sleep(0.1)

