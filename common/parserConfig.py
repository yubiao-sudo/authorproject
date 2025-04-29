import os
import configparser
from common.logger import Logger


logger = Logger(logger='ParserConfig').get_log()


class ParserConfig(object):

    def __init__(self):
        self.url = ''
        self.browserType = ''

    def get_config(self):
        """
            获取当前路径
        """
        root_dir = os.path.dirname(os.path.abspath('.'))
        logger.info('系统根路径：%s' % root_dir)
        config = configparser.ConfigParser()
        file_path = root_dir + r'\config\config.ini'
        logger.info('获取当前路径：%s' % file_path)
        config.read(file_path, encoding='UTF-8')
        return config

    # 获取驱动类型
    def get_browser_type(self):
        return self.get_config().get('browserType', 'browserName')

    # 获取路径
    def get_url(self):
        return self.get_config().get('testServer', 'url')

    # 获取数据配置信息
    def get_db(self):
        host = self.get_config().get('testdb', 'host')
        user = self.get_config().get('testdb', 'user')
        password = self.get_config().get('testdb', 'password')
        database = self.get_config().get('testdb', 'database')
        return host, user, password, database
