import os
from common.logger import Logger
logger = Logger(logger="Report").get_log()


class Report:
    def html_report(self, case):
        if case != '':
            try:
                os.system('python -m pytest ../testcase/{}.py --alluredir=./report_{}/report-xml/'.format(case, case))
                os.system('allure generate ./report_{}/report-xml -o ./report_{}/report/ --clean'.format(case, case))
                logger.info("报告已生成：{}".format(os.path.abspath('../report_{}/report/index.html').format(case)))
                os.system(r'allure open -h 127.0.0.1 -p 8083 ./report_{}/report'.format(case))
                logger.info('报告正在生成中、将自动弹出、请稍后。。。')
            except FileNotFoundError as e:
                logger.error('报告生成失败，请检查文件路径或命令行{}'.format(e))
        else:
            try:
                os.system('python -m pytest ../testcase/ --alluredir=./report_all/report-xml/')
                os.system('allure generate ./report_all/report-xml -o ./report_all/report/ --clean')
                logger.info("报告已生成：{}".format(os.path.abspath('../report_all/report/index.html')))
                os.system(r'allure open -h 127.0.0.1 -p 8083 ./report_all/report')
                logger.info('报告正在生成中、将自动弹出、请稍后。。。')
            except FileNotFoundError as e:
                logger.error('报告生成失败，请检查文件路径或命令行{}'.format(e))


if __name__ == '__main__':
    r = Report()
    r.html_report('BaiduPage_test')
