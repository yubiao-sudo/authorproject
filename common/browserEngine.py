import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.edge.service import Service as EdgeService
# webdriver_manager 第三方库，自动识别当前运行环境下系统信息以及对应浏览器信息，启动下载对应的webdriver，再也不用担心webdriver版本问题
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from common.parserConfig import ParserConfig
from common.logger import Logger

logger = Logger(logger='BrowserEngine').get_log()


class BrowserEngine(object):
    """
        定义浏览器引擎，根据browser值，控制启动不同浏览器，主要是IE、chrome、Firefox
    """

    def __init__(self):
        pass

    def get_browser(self):

        # 获取浏览器类型
        browser = ParserConfig().get_browser_type()
        logger.info('选择 %s 浏览器' % browser)
        # 获取测试环境
        url = ParserConfig().get_url()
        logger.info('运行环境 %s' % url)
        # 根据浏览类型启动相应的driver
        if browser == 'FireFox':
            driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()))
            # driver = webdriver.Firefox()
        elif browser == 'Chrome':
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            # driver = webdriver.Chrome()
        elif browser == 'IE':
            # driver = webdriver.Ie(service=IeService(IEDriverManager().install()))
            driver = webdriver.Ie()
        elif browser == 'Edge':
            driver = webdriver.Ie(service=EdgeService(EdgeChromiumDriverManager().install()))
        elif browser == 'Opera':
            driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        else:
            # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)
        return driver


if __name__ == '__main__':
    browser = BrowserEngine()
    driver = browser.get_browser()
    time.sleep(2)
    driver.quit()
