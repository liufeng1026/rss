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
    gzh_list = getGzhList()
    print ("获取要跟踪的公众号列表为:", gzh_list)
    # 遍历字典列表
    for key, value in gzh_list.items():
        art = gzhArticle.getNewGzhArticle(key)
        print ("公众号:{key}的历史文章为:{value}".format(key=key,value=value))
        if art is not None and art['title'] != value:
            print ("公众号:{key}的最新文章为:{value}".format(key=key, value=art['title']))
            qqmail.send_mail(title=art['title'], content=art['href'], receiver='76816025@qq.com')
            gzh_list[key] = art['title']
    # 更新公众号列表并回写文件
    print ("更新跟踪的公众号列表为:", gzh_list)
    updateGzhList(gzh_list)
    schedule.enter(inc, 0, executor, (inc,))


def getGzhList():
    gzh_list = {}
    with open('gzhList.txt', 'r') as f:
        for line in f.readlines():
            if len(line.strip('\n')) > 3:
                k, v = line.split(' ', 2)
                gzh_list[k] = v.strip('\n')
    return gzh_list


def updateGzhList(gzh_list):
    with open('gzhList.txt', 'w+') as f:
        # 遍历字典列表
        for k, v in gzh_list.items():
            f.write(k + ' ' + v)
            f.write('\n')


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
print ("开始执行获取微信公众号任务")
main(600)
# executor(600)
