import pymysql
from common.parserConfig import ParserConfig


class DBConnect(object):
    params = ParserConfig().get_db()
    conn = pymysql.connect(host=params[0], user=params[1], password=params[2], db=params[3], charset='utf8',
                           cursorclass=pymysql.connections.DictCursor)
