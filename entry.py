#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from WeixinArticle import WxGzhArticle
from qqmail import qqMail
import scheduleTask
import sched
import time
from datetime import datetime


def executor(inc):
    gzhArticle = WxGzhArticle()
    qqmail = qqMail()
    # 定义一个公众号列表
    gzh_list = ['OK数码2016']
    for gzh in gzh_list:
        art = gzhArticle.getNewGzhArticle(gzh)
        if art is not None:
            qqmail.send_mail(title=art['title'], content=art['href'], receiver='76816025@qq.com')
    schedule.enter(inc, 0, executor, (inc,))


# # 添加调度任务//TODO:待验证是否可用
# # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
# scheduleTask.scheduler.add_job(executor, 'interval', seconds=3)
# # 启动调度任务
# scheduleTask.scheduler.start()
# print ("dsf")


# 初始化sched模块的 scheduler 类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)

# 默认参数60s
def main(inc=60):
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    schedule.enter(0, 0, executor, (inc,))
    schedule.run()


# 10s 输出一次
main(60)
# executor(10)