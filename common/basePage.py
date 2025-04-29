from selenium.common import NoSuchElementException
from common.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

# create a logger instance
logger = Logger(logger="BasePage").get_log()


# 封装一些常用的方法
class BasePage:

    def __init__(self, driver):
        self.alter = None
        self.driver = driver

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info('输入前清除输入文本框中的内容')
        except NameError as e:
            logger.error('无法在输入框中清除%s' % e)

    def get_text(self, selector):
        el = self.find_element(selector)
        logger.info('文本内容为：'+el.text)
        return el

    # 元素定位
    def find_element(self, selector):
        element = ''
        if '=>' not in selector:
            return self.driver.find_element(By.ID, selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element(By.ID, selector_value)
                logger.info(
                    "找到了元素 {} ,{} 定位成功  元素值为: {} ".format(element.tag_name, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("没有找到这样的元素: {}".format(e))
                self.get_windows_img()  # 截图
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element(By.NAME, selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by(By.CLASS_NAME, selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element(By.LINK_TEXT, selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element(By.TAG_NAME, selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element(By.XPATH, selector_value)
                logger.info("已找到了元素 {}, {} 定位成功  元素属性为: {} ".format(element.tag_name, selector_by,
                                                                                   selector_value))
            except NoSuchElementException as e:
                logger.error("没有找到这样的元素: {}".format(e))
        elif selector_by == "s" or selector_by == 'css_selector':
            element = self.driver.find_elementr(By.CSS_SELECTOR, selector_value)
        else:
            raise NameError("请输入有效类型的定位元素.")

        return element

    # 输入
    def send_key(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info('内容: \'{}\'  输入成功'.format(text))
        except NameError as e:
            logger.error('输入框输入失败{}' % e)
            # 需要截图

    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("元素 {} 被点击.".format(el.tag_name))
        except NameError as e:
            logger.error("无法单击元素 {}".format(e))

    # 保存截图至目录
    def get_windows_img(self, obj, element):
        os_path_file = os.path.dirname(os.path.abspath('.'))
        if not os.path.exists(os_path_file + r'\screenshots\\' + obj):
            os.mkdir(os_path_file + r'\screenshots\\' + '{}'.format(obj))
            print(obj + "目录创建成功")
        else:
            print("目录已存在")
        file_path = os_path_file + '/screenshots/{}/'.format(obj)
        rq = time.strftime('{}_%Y年%m月%d日%H时%M分%S秒'.format(element), time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info(
                r"已截取屏幕截图并保存到文件夹 :"
                + os_path_file + '/screenshots/{}下'.format(obj))
        except NameError as e:
            logger.error("截屏失败! {}".format(e))

    # 获取页面标题
    def get_page_title(self):
        logger.info('当前页面标题是{}'.format(self.driver.title))
        return self.driver.title

    # def get_text(self,selector):
    #     el=self.find_element(selector)
    #     return

    # 获取浏览器地址
    def get_current_url(self):
        logger.info('获取当前地址{}'.format(self.driver.current_url))
        return self.driver.current_url

    # 切换弹窗 执行弹窗其他操作
    def switch_to_alter(self):
        try:
            self.alter = self.driver.switch_to_alter()
            logger.info("执行切换弹窗操作成功")
        except NameError as e:
            logger.error("切换弹窗失败! %s" % e)

    def get_alter_value(self):
        try:
            self.alter.text()
            logger.info("执行弹窗操作-获取文本成功")
        except NameError as e:
            logger.error("获取文本失败! %s" % e)

    def alter_accept(self):
        try:
            self.alter.accept()
            logger.info("执行弹窗操作--点击确定成功")
        except NameError as e:
            logger.error("执行弹窗操作--点击确定失败！%s" % e)

    def alter_dismiss(self):
        try:
            self.alter.dismiss()
            logger.info("执行弹窗操作--点击取消成功")
        except NameError as e:
            logger.error("执行弹窗操作--点击取消失败! %s" % e)

    # 强制等待
    def time_sleep(self, number):
        time.sleep(number)

    # 鼠标移动
    def move_to_element(self, selector):
        ActionChains(self.driver).move_to_element(self.find_element(selector))

    # 关闭浏览器页面
    def close(self):
        self.driver.close()
        logger.info("页面已关闭")

    # 关闭浏览器
    def quit(self):
        self.driver.quit()
        logger.info("浏览器已关闭")
