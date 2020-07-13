# -*- coding: utf-8 -*-
# 开发人员   ：黎工
# 开发时间   ：2020/6/24  14:42 
# 文件名称   ：schedule_test.PY
# 开发工具   ：PyCharm

import schedule
import time
import datetime

def job():
    print("I'm working..." + str(datetime.datetime.now()))

print(datetime.datetime.now())
schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("15:20").do(job)
schedule.every(5).to(10).days.do(job)   # 每隔5到10天执行
schedule.every().monday.do(job)
schedule.every().wednesday.at("15:10").do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)