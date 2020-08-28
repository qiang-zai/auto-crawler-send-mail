import requests
import xlwt
import os
import datetime
from lxml import etree
from settings import base_path, data_storage_folder_name, file_name, file_format


def init_url_list(number_pages_crawled):
    """初始化url列表"""
    return ["http://www.ccgp.gov.cn/zcfg/bbdw/czb/index.htm"] + [
        "http://www.ccgp.gov.cn/zcfg/bbdw/czb/index_{}.htm".format(i) for i in range(1, number_pages_crawled)]


def run_spider(url_list):
    """运行爬虫"""
    # [{"title": "xxx", "red_file_number": "xxx", "release_date": "xxx"}, {}, {}...]
    data_list = []

    for n, url in enumerate(url_list):
        response = requests.get(url)

        html_data = etree.HTML(response.content.decode())
        row_node_list = html_data.xpath("//*[@class='c_list_zcfg']/li")
        for row_node in row_node_list:
            title = row_node.xpath("./a/@title")[-1]
            release_date = row_node.xpath("./span[1]/text()")[-1]
            red_file_number = row_node.xpath("./span[2]/text()")[-1] if row_node.xpath("./span[2]/text()") else "无"
            data_list.append({"title": title, "red_file_number": release_date, "release_date": red_file_number})
        print("第{}页已完成数据爬取".format(n))
    return data_list


def write_to_excel(data_list):
    """下入excel"""
    # 创建一个workbook设置编码
    workbook = xlwt.Workbook(encoding="utf-8")
    # 创建一个worksheet
    work_sheet = workbook.add_sheet("data")
    # 设置样式
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style = xlwt.XFStyle()
    style.alignment = alignment
    # 下入excel
    for column_num, column_name in enumerate(data_list[0]):
        work_sheet.write(0, column_num, label=column_name, style=style)
    for row_num, row_data in enumerate(data_list, start=1):
        for column_num, column_name in enumerate(row_data):
            work_sheet.write(row_num, column_num, label=row_data[column_name], style=style)
    if not os.path.exists(os.path.join(base_path, data_storage_folder_name)):
        os.mkdir(data_storage_folder_name)
    file_path = os.path.join(base_path, data_storage_folder_name) + datetime.datetime.now().strftime(
        file_format) + file_name
    workbook.save(file_path)
    return file_path
