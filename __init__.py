"""
AScript 工程入口
ESP32 蓝牙 HID 基础测试（导入后直接执行）
"""

from ascript.android import plug
plug.load("esp32")
from esp32 import BleDevice
from ascript.android.system import Device
import time

print("===== ESP32 HID 基础测试开始 =====")

display = Device.display()
w = display.widthPixels
h = display.heightPixels
print("当前屏幕分辨率:", w, "x", h)

print("正在尝试连接 ESP32 蓝牙 HID...")
ble = BleDevice()

print("设备名称:", ble.get_name())
print("MAC地址:", ble.get_mac_address())

if ble.is_conncted():
    print("已连接成功")
else:
    print("未连接，尝试重连...")
    if ble.re_connect():
        print("重连成功")
    else:
        print("重连失败，请先在系统蓝牙里配对 AS 开头的设备")
        raise SystemExit

time.sleep(1)

cx = w // 2
cy = h // 2
print("正在点击屏幕中心:", cx, cy)
ble.click(cx, cy)
time.sleep(1.5)

print("正在执行滑动测试...")
ble.slide(cx, cy + 200, cx, cy - 200, dur=600)
time.sleep(1.5)

print("正在打开后台切换器...")
ble.recent()
time.sleep(2)

print("正在按 Home 键回桌面...")
ble.home()
time.sleep(1)

print("===== 测试结束 =====")
print("请观察：连接、中心点击、滑动、后台、回桌面是否正常")
