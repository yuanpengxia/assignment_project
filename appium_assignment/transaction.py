from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestTransaction():
    def setup_class(self):
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
        # self.driver.implicitly_wait(5)

    def teardown_class(self):
        sleep(2)
        self.driver.quit()
        pass

    def test_search(self):
        print("这是一个搜索案例")
        sleep(3)
        self.driver.find_element(MobileBy.XPATH,
                                 f"//*[@resource-id='com.bkt.exchange:id/tv_indicator'and @text='交易']").click()
        self.driver.find_element(MobileBy.CLASS_NAME, "android.widget.ImageView").click()

    @pytest.mark.parametrize("cointype",['BKK','BNB','ETH'])
    def test_bkk(self,cointype):
        self.driver.find_element(MobileBy.ID, "com.bkt.exchange:id/coin_edit").send_keys(cointype)
        sleep(5)
        print(self.driver.find_element(MobileBy.XPATH,
                                       f"//*[@resource-id='com.bkt.exchange:id/pair' and contains(@text,'{cointype}')]"))
        sleep(2)
        # 返回到上一页面
        self.driver.back()
        # self.driver.back()
    #
    # def test_add_favorites(self):
    #     pass
if __name__ == '__main__':
    pytest.main()