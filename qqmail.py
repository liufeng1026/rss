#! /usr/bin/env python
# coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


class qqMail:

    def __init__(self):
        # qq邮箱smtp服务器
        self.host_server = 'smtp.qq.com'
        self.sender_qq = '2685308159@qq.com'
        self.sender_mail = '2685308159@qq.com'
        self.third_token = 'mgrlaxknqznwdfib'

    def send_mail(self, title, content, receiver):
        # ssl登录
        smtp = SMTP_SSL(self.host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(0)
        smtp.ehlo(self.host_server)
        smtp.login(self.sender_qq, self.third_token)

        msg = MIMEText(content, "html", 'utf-8')
        msg["Subject"] = Header(title, 'utf-8')
        msg["From"] = self.sender_mail
        msg["To"] = Header("接收者", 'utf-8')  ## 接收者的别名

        smtp.sendmail(self.sender_mail, receiver, msg.as_string())
        print ("发送邮件成功，标题：{subject}@@@@@内容：{content}".format(subject = title, content = content))
        smtp.quit()
