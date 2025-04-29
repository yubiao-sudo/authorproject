import os
import yaml
from common.logger import Logger

logger = Logger(logger='ParserYaml').get_log()


class ParserYaml(object):

    def read_yaml_data(self, file_name):
        file_path = os.path.dirname(os.path.abspath('.')) + r'\data\%s' % file_name
        logger.info('yaml文件路径%s' % file_path)
        yaml_data = open(file_path, 'r', encoding='UTF-8')
        logger.info('执行到open没有报错')
        data = yaml.load(yaml_data, Loader=yaml.FullLoader)
        logger.info('读取yaml文件%s' % data)
        logger.info('打印data长度 %s' % len(data))
        return data
