import smtplib
from email.header import Header
from email.mime.text import MIMEText

from .variable import MAIL_HOST, MAIL_PASSWD, MAIL_USER, MAIL_FROM


def send_email(mail_title, mail, subject):
    """

    :param mail_title: 邮件标题
    :param mail: 接受人
    :param subject: 邮件主题
    :return:
    """
    sender = 'from@runoob.com'
    print(1111)
    message = MIMEText(mail_title, 'plain', 'utf-8')
    message['From'] = Header(MAIL_FROM, 'utf-8')
    message['To'] = Header(mail, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(MAIL_HOST, 587)  # 25 为 SMTP 端口号
        smtpObj.login(MAIL_USER, MAIL_PASSWD)
        smtpObj.sendmail(sender, mail, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e: 
        print("邮件发送失败",e)



