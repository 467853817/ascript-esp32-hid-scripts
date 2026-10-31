"""
按官方插件页 (https://www.ascript.cn/plug/?id=103) 写法的最小测试
先验证：连接 + 固定坐标点击 + 屏幕中心点击 + home
"""

from ascript.android import plug
plug.load("esp32:4.7.0")
from esp32 import BleDevice
from ascript.android.system import Device
import time

print("===== 官方写法最小测试 =====")

ble = BleDevice()
print("名称:", ble.get_name())
print("MAC:", ble.get_mac_address())

if ble.is_conncted():
    print("已连接")
else:
    print("未连接，尝试 re_connect...")
    ok = ble.re_connect()
    print("重连结果:", ok)
    if not ok:
        print("失败：请到 设置-蓝牙 确认已配对并连接 AS 开头设备")
        raise SystemExit

time.sleep(0.5)

# 官方文档示例坐标（先试固定点）
print("点击官方示例坐标 394,2116")
ble.click(394, 2116)
time.sleep(1.5)

# 再点屏幕中心
d = Device.display()
w, h = d.widthPixels, d.heightPixels
print("分辨率:", w, "x", h)
cx, cy = w // 2, h // 2
print("点击中心:", cx, cy)
ble.click(cx, cy)
time.sleep(1.5)

print("执行 home")
ble.home()
time.sleep(1)

print("===== 测试结束 =====")
print("若日志有「已连接」但屏幕无反应：")
print("1. 确认固件是官网 AS 蓝牙固件，蓝牙名以 AS 开头")
print("2. 系统蓝牙里该设备状态为已连接")
print("3. 可尝试忽略设备后重新配对")
