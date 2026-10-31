# ascript-esp32-hid-scripts

对齐官方插件文档：https://www.ascript.cn/plug/?id=103

## 使用（只下载导入，不要粘贴代码）

1. https://github.com/467853817/ascript-esp32-hid-scripts
2. Code → Download ZIP
3. AScript 导入工程
4. 系统蓝牙配对并连接 **AS** 开头设备
5. 运行

## 官方关键写法

```python
from ascript.android import plug
plug.load("esp32:4.7.0")
from esp32 import BleDevice
ble = BleDevice()
print("名称", ble.get_name())
if ble.is_conncted():
    print("已连接")
ble.click(394, 2116)
```

## 无屏幕反应时优先查硬件

- 固件：官网下载的 AS 蓝牙固件，烧录后蓝牙名以 AS 开头
- 配对：设置 → 蓝牙 → AS... → 已连接
- 插件：使用 `esp32:4.7.0`
