# -*- coding: utf-8 -*-

# 代理IP池程序入口
import re
import time

import schedule

import config
from crawler import get_all_proxies
from process import DataProcessor
from validate import validate, concat_proxy

# 数据处理器
dp = DataProcessor()


def crawler_task():
    for item in get_all_proxies():
        # cannot unpack non-iterable bool object
        flag, level = validate(*item)
        if not flag:
            continue
        else:
            # 加入代理IP池中
            dp.save(concat_proxy(item), level)
    print('[{}]完成爬虫任务'.format(time.ctime()))


def validate_task():
    # 从代理IP池中获取数据
    for proxy, level in dp.query():
        # 执行校验，剔除无效数据
        flag, level2 = validate(*re.split(r'(://|:)', proxy)[::2])
        if not flag:
            dp.remove(proxy, level)
        else:
            # 加入代理IP池中
            dp.save(proxy, level2)
            # 如果代理级别发生变化，则移除原集合中的代理IP
            if level != level2:
                dp.remove(proxy, level)
    print('[{}]完成校验任务'.format(time.ctime()))


if __name__ == '__main__':
    print('[{}]启动代理IP池维护任务'.format(time.ctime()))

    # 手动执行一次，定时任务将会在下一个周期才开始执行
    crawler_task()

    # 启动爬虫定时任务
    schedule.every(config.crawler_task_interval).seconds.do(crawler_task)
    # 启动IP有效性校验任务
    schedule.every(config.validate_task_interval).seconds.do(validate_task)

    while True:
        schedule.run_pending()
        time.sleep(1)
