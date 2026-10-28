# AScript ESP32 Bluetooth HID 脚本仓库

用于在 AScript（安卓）上通过 ESP32 蓝牙 HID 进行物理级点击、滑动、输入等自动化脚本。

## 仓库结构

```
ascript-esp32-hid-scripts/
├── README.md
├── tests/
│   └── test_basic_hid.py      # 基础连接与点击测试脚本
└── scripts/                 # 后续正式业务脚本放这里
```

## 使用前准备

1. ESP32 已烧录 AScript 官方 HID 固件（蓝牙版）
2. 手机蓝牙已配对 AS 开头的设备
3. 安装并打开 AScript App
4. 确保 `esp32` 插件已加载

## 快速开始

1. 把 `tests/test_basic_hid.py` 内容复制到 AScript 编辑器
2. 运行脚本
3. 观察日志和手机实际反应

## 官方文档

- [ESP32-HID 外设 Android](https://www.ascript.cn/docs/android/esp32/)
- [HID 外设总览](https://www.ascript.cn/hid/)
