from common.basePage import BasePage,logger


class baiduPage(BasePage):
    pathList = {
        '搜索框': 'id=>kw',
        '百度一下按钮': 'id=>su',
        '事件名称3': 'path3',
        '事件名称4': 'path4',
        '断言': 'xpath=>//*[@id="content_left"]/div',
    }

    # def qurey_world(self, text):
    #     '''此页面存放定位元素'''
    #     self.click(self.pathList['搜索框'])
    #     self.send_key(self.pathList['搜索框'], text)
    #     self.click(self.pathList['百度一下按钮'])

    def qurey_world(self,listone,text):
        '''此页面存放定位元素'''
        self.click(listone[0][0])
        print(listone)
        self.send_key(listone[0][0], text)
        self.click(listone[0][1])


    def assert_text(self,listone):
        t = self.get_text(listone[0][2])
        return t

