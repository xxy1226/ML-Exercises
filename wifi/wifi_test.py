# coding:utf-8

import pywifi
from pywifi import const

# 判断是否已经连接到WiFi

def gic():
    """检查网络连接状态"""
    # 创建一个无线对象
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # print(ifaces.name())
    # 列表
    # print(ifaces)
    # 打印网卡连接状态 0 未连接到WiFi环境 4 已连接
    # print(ifaces.status())
    if ifaces.status() == const.IFACE_CONNECTED:
        print("已连接")
    else:
        print("未连接")

def bies():
    """扫描附近的WiFi"""
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    # 扫描WiFi
    iface.scan()
    # 获取扫描结果
    result = iface.scan_results()
    for name in result:
        # ssid WiFi的名称
        print(name.ssid)

bies()