import time
import pytest
from selenium.webdriver.common.by import By
from common.browserEngine import BrowserEngine
from pages.BaiduPage import baiduPage


@pytest.fixture(params=['', ''])
def Data_init(request):
    return request


class Test_casePage:

    # 全部case执行开始前初始化
    def setup_class(self):
        browser = BrowserEngine()
        self.driver = browser.get_browser()
        print("开始执行")

    # 单条用例执行前初始化环境
    def setup(self):
        pass

    # 单条用例执行后清理环境
    def teardown(self):
        self.driver.quit()

    # baiduPage页面查询业务用例
    def test1_query(self):
        obj = 'baidu_queryWorld'
        list = ['原神', '鸣潮', '星穹铁道', '率土之滨', '中国']
        for world in list:
            b = baiduPage(self.driver)
            b.qurey_world(world)
            self.driver.implicitly_wait(10)
            t = b.assert_text().text
            time.sleep(2.5)
            b.get_windows_img(obj, world)
            assert world in t, '测试不通过'
            self.driver.back()

    # casePage页面创建案例业务用例
    @pytest.mark.skip()
    def test2_createCase(self):
        t = self.driver.find_element(By.XPATH, '//*[@id="content_left"]/div[1]')
        print(t.text)

    # 全部case执行完毕清理
    def teardown_class(self):
        print("已全部执行完毕")
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
