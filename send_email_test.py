# -*- coding: utf-8 -*-
# 开发人员   ：黎工
# 开发时间   ：2020/6/24  10:22 
# 文件名称   ：send_email_test.PY
# 开发工具   ：PyCharm

import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication
import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=5)
    yesterday = today - oneday
    return yesterday


def send_email(smtpHost,sendAddr,password,recipientAddrs,subject,content,cc):
    catalog = str(getYesterday())
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    msg['Cc'] = cc
    txt = email.mime.text.MIMEText(content,'plain','utf-8')
    msg.attach(txt) # 邮件正文内容
    # 添加附件
    part = MIMEApplication(open('../zip_file/'+'央企新冠每日舆情'+catalog+'.zip','rb').read())
    part.add_header('Content-Disposition','attachment',filename='央企新冠每日舆情'+catalog+'.zip')
    msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect(smtpHost,'25')
    smtp.login(sendAddr,password)
    smtp.sendmail(sendAddr,[recipientAddrs,cc], msg.as_string()) # 括号中对应的是发件人邮箱，收件人邮箱，发送邮件
    print('发送成功！')
    smtp.quit()


def run():
    try:
        subject = '央企新冠每日舆情'
        content = '您好,\n     附件是央企新冠每日舆情，请查收。谢谢！\n                                                  技术部'
        # smtpHost = 'smtp.exmail.qq.com' # SMTP服务器
        smtpHost = 'smtp.126.com' # SMTP服务器
        sendAddr = ''   # 发件人邮箱账号
        password = ''   # 发件人邮箱密码
        recipientAddrs = ''   # 收件人邮箱账号
        cc = ''   # 抄送人邮箱账号
        send_email(smtpHost,sendAddr,password,recipientAddrs,subject,content,cc)
    except Exception as err:
        print('无法发送邮件',err)


if __name__ == '__main__':
    run()