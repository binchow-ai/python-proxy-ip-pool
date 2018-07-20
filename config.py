# -*- coding: utf-8 -*-
# 提供工程全局配置
import os

default_user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) ' \
                     'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/55.0.2883.87 Safari/537.36'
query_max_page = 5

# 192.168.0.105 是我的测试服务器，请忽略(实际应用肯定是要指定的)
redis_host = os.environ.get('REDIS_HOST', '192.168.0.105')
redis_port = os.environ.get('REDIS_PORT', 6379)

# 无效代理IP缓存时长，单位：H
cache_expire_interval = 24

# 测试代理超时设置
better_timeout = 1.0
normal_timeout = 3.0

# 测试代理URL
target_http_url = 'http://api.zlikun.com/ip'
target_https_url = 'https://api.zlikun.com/ip'

# 定时任务频率设置，单位：秒
crawler_task_interval = 300
validate_task_interval = 90
