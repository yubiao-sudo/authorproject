from report.HTML_Report import Report


class Boot:
    def __init__(self, parameter):
        self.btpms = parameter

    def boot(self):
        report_all = Report()
        report_all.html_report(self.btpms)


if __name__ == '__main__':
    parameter = ''
    bt = Boot(parameter)
    bt.boot()
