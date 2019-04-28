import os
from appium import webdriver
import time

apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '8.0.0'  # 设备系统版本
desired_caps['deviceName'] = '小米手机'  # 设备名称
# 测试apk包的路径
desired_caps['app'] = apk_path + '\\app\\yixinli20190404.apk'
#不需要每次都安装apk
desired_caps['noReset'] = True
# 应用程序的包名
desired_caps['appPackage'] = 'com.xinli.yixinli';
desired_caps['appActivity'] = 'com.xinli.yixinli.activity.LauncherActivity'
# 如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之

time.sleep(1)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) ; # 启动app

time.sleep(10); #app启动后等待20秒，方便元素加载完成

#定位搜索框
driver.find_element_by_id('com.xinli.yixinli:id/tab_course').click()


driver.quit()