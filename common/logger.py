import logging
import time
import os


class Logger(object):
    def __init__(self, logger):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('{}_%Y年%m月%d日 %H时%M分%S秒'.format(logger), time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + r'/logs/'
        log_name = log_path + rq + '.log'

        fh = logging.FileHandler(log_name, mode='a+', encoding='UTF-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger 添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger
