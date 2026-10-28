# AScript ESP32 Bluetooth HID 脚本仓库

用于在 AScript（安卓）上通过 ESP32 蓝牙 HID 进行物理级点击、滑动、输入等自动化脚本。

## 工程结构（标准 AScript 工程）

```
ascript-esp32-hid-scripts/
├── __init__.py          # 工程入口（必须）
├── main.py              # ESP32 HID 基础测试脚本
├── README.md
└── tests/               # 历史测试文件（可忽略）
```

## 使用前准备

1. ESP32 已烧录 AScript 官方 HID 固件（蓝牙版）
2. 手机蓝牙已配对 AS 开头的设备
3. 安装并打开 AScript App
4. 确保 `esp32` 插件已加载

## 推荐导入方式（公网 Web-IDE）

1. 打开仓库：https://github.com/467853817/ascript-esp32-hid-scripts
2. 点击右上角 **Code** → **Download ZIP**
3. 解压后，进入 AScript 公网开发者构建网站
4. 点击左侧 **上传工程**
5. 选择解压后的文件夹（或直接选 zip）进行导入
6. 导入成功后点击运行

> 工程根目录已包含 `__init__.py`，符合 AScript 导入要求。

## 测试内容

运行后会依次测试：

1. 连接 ESP32 蓝牙 HID
2. 点击屏幕中心
3. 上下滑动
4. 打开后台任务切换器
5. 按 Home 键回桌面

## 官方文档

- [ESP32-HID 外设 Android](https://www.ascript.cn/docs/android/esp32/)
- [HID 外设总览](https://www.ascript.cn/hid/)
