# -*- coding:utf-8 -*-
__author__ = 'qiangzai'

import settings
from send_mail import SendMailService
from tools import init_url_list, run_spider, write_to_excel

def execute_crawler():

    url_list = init_url_list(settings.number_pages_crawled)
    data_list = run_spider(url_list)
    file_path = write_to_excel(data_list)
    ret = SendMailService().send(settings.RECEIVER, settings.RECEIVER_NICK, settings.SUBJECT, file_path,
                                 settings.CONTENT)
    return ret


if __name__ == '__main__':
    execute_crawler()
