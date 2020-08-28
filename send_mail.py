import os
import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendMailService(object):
    def __init__(self, sender=None, pwd=None, From=None):
        self.sender = sender or settings.SENDER_MAIL_ACCOUNT  # 发件人邮箱
        self.pwd = pwd or settings.SENDER_MAIL_PASSWORD  # 发件人密码
        self.From = From or settings.From  # 发件人昵称

    def send(self, receivers, to, subject, file_path, content=""):
        """
        :param receivers:   收件人邮件账号
        :param to:          收件人邮箱昵称
        :param subject:     邮件的主题
        :param content:     邮件内容
        :return: True/False
        """
        flag = True

        # message = MIMEText(content)
        # message["From"] = Header(self.From, "utf-8")
        # message["To"] = Header(to, "utf-8")
        # message["Subject"] = Header(subject, "utf-8")

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message["From"] = Header(self.From, "utf-8")
        message["To"] = Header(to, "utf-8")
        message["Cc"] = self.sender
        message["Subject"] = Header(subject, "utf-8")
        # 添加==>邮件正文内容
        message.attach(MIMEText(content, "plain", "utf-8"))
        # 添加==>附件1
        att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1.add_header('content-disposition', 'attachment', filename=('utf-8', '', file_path.split("/")[-1]))
        message.attach(att1)
        try:
            # (SMTP服务器地址, SMT服务器端口)
            ssl_server = smtplib.SMTP_SSL(settings.SMTP_SERVER, settings.SMTP_PORT)
            # (发件人邮箱, 发件人密码这个密码是授权密码)
            ssl_server.login(self.sender, self.pwd)
            # (发件人邮箱, (收件人列表,), 消息)
            ssl_server.sendmail(self.sender, receivers, message.as_string())
            # 关闭连接
            ssl_server.quit()
        except Exception as e:
            print(e)
            flag = False
        return flag


if __name__ == '__main__':
    file_path = '/Users/qiangzai/Desktop/PracticeCode/Interview-question-code/automatic-crawler-code/data/2020年08月26日17时-data.xls'
    ret = SendMailService().send(("china_qiangzai@163.com",), "zaizai",
                                 "[招标]本周数据", file_path,
                                 "本周招标数据")
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
