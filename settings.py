import os

# 爬取的页数
number_pages_crawled = 0
# 项目路径
base_path = os.path.dirname(os.path.abspath(__file__))
# 数据存储名称
data_storage_folder_name = "data/"
# 文件名称
file_name = "-data.xls"
file_format = "%Y年%m月%d日%H时"

# 邮件相关
From = "qiangzai"  # 发件人邮箱昵称
SMTP_SERVER = "smtp.163.com"  # SMTP 服务器
SMTP_PORT = 465  # SMTP端口
SENDER_MAIL_ACCOUNT = "xxxxxxxxxxx@163.com"  # 发送方邮箱
SENDER_MAIL_PASSWORD = "xxxxxxxxxxxxx"  # 发送方客户端密码
RECEIVER = ("xxxxxxxxxx@163.com",)  # 接收方列表
RECEIVER_NICK = "boss"  # 接收方昵称
SUBJECT = "【招标】本周最新数据"  # 邮件标题
CONTENT = "您好, BOSS!这是最新的招标数据"  # 邮件内容
