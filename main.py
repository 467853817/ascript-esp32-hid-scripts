"""
AScript ESP32 Bluetooth HID 基础测试脚本

测试目的：
1. 能否正常连接到 ESP32 蓝牙 HID 设备
2. 能否获取设备名称和 MAC 地址
3. 能否执行点击（屏幕中心）
4. 能否执行简单滑动
5. 能否打开后台任务切换器（recent）
6. 能否按 Home 键返回桌面
"""

from ascript.android import plug
plug.load("esp32")
from esp32 import BleDevice
from ascript.android.system import Device
import time

def main():
    print("===== ESP32 HID 基础测试开始 =====")

    # 1. 获取屏幕信息
    display = Device.display()
    w = display.widthPixels
    h = display.heightPixels
    print(f"当前屏幕分辨率: {w} x {h}")

    # 2. 连接设备
    print("正在尝试连接 ESP32 蓝牙 HID...")
    ble = BleDevice()

    name = ble.get_name()
    mac = ble.get_mac_address()
    print(f"设备名称: {name}")
    print(f"MAC地址: {mac}")

    if ble.is_conncted():
        print("✅ 已连接成功")
    else:
        print("⚠️ 未连接，尝试重连...")
        if ble.re_connect():
            print("✅ 重连成功")
        else:
            print("❌ 重连失败，请检查蓝牙配对状态")
            return

    time.sleep(1)

    # 3. 点击屏幕中心
    cx = w // 2
    cy = h // 2
    print(f"正在点击屏幕中心: ({cx}, {cy})")
    ble.click(cx, cy)
    time.sleep(1.5)

    # 4. 简单滑动（从中心向上滑一小段）
    print("正在执行滑动测试...")
    ble.slide(cx, cy + 200, cx, cy - 200, dur=600)
    time.sleep(1.5)

    # 5. 打开后台任务切换器
    print("正在打开后台切换器...")
    ble.recent()
    time.sleep(2)

    # 6. 按 Home 键回桌面
    print("正在按 Home 键回桌面...")
    ble.home()
    time.sleep(1)

    print("===== 测试结束 =====")
    print("请观察：")
    print("1. 日志里是否显示“已连接成功”")
    print("2. 手机是否有中心点击反应")
    print("3. 是否有上下滑动")
    print("4. 是否打开了后台任务切换器")
    print("5. 是否回到了桌面")

if __name__ == "__main__":
    main()
