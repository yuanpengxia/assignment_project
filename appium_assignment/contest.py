from time import sleep

from appium import webdriver


def setup(self):
    desire_cap = {
    "platformName": "Android",
    "deviceName": "7XBNW19910007839",
    "appPackage": "com.bkt.exchange",
    "appActivity": ".activity.StartPageActivity",
    # 支持中文输入
    "unicodeKeyBoard": "true",
    "resetKeyBoard": "true",
    # 绕过弹窗
    "noReset": True,
    # 不需要重启，直接按照上次停留的页面继续操作（提升运行速度）
    "dontStopAppOnReset": True,
    # 跳过安装，权限等设置等操作（提升运行速度）
    "skipDeviceInitialization": True
    }
    self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
    self.driver.implicitly_wait(5)


def teardown(self):
    sleep(2)
    self.driver.quit()
    pass