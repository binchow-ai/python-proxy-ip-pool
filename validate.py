# -*- coding: utf-8 -*-


# 代理IP有效性验证，使用requests库检查，其代理设置参考：
# http://cn.python-requests.org/zh_CN/latest/user/advanced.html#proxies
import time
from concurrent.futures.thread import ThreadPoolExecutor

import requests

import config
from crawler import get_all_proxies


def concat_proxy(item):
    """
    将元组组装成代理字符串
    :param item:
    :return:
    """
    return '{}://{}:{}'.format(*item)


def validate(protocol, ip, port):
    """
    检查代理IP有效性
    :param protocol:
    :param ip:
    :param port:
    :return:
    (True, 1) 表示有效且优质
    (True, 0) 表示有效但普通
    False     表示无效
    """
    if check(protocol, ip, port, config.better_timeout):
        return True, 1
    elif check(protocol, ip, port, config.normal_timeout):
        return True, 0
    else:
        return False, None


def check(protocol, ip, port, timeout=0.5):
    """
    内部函数，检查代理IP是否有效
    :param protocol:
    :param ip:
    :param port:
    :param timeout:
    :return:
    """
    protocol = protocol.lower()
    try:
        # 根据协议自动切换测试URL
        target_url = config.target_https_url
        if protocol == 'http':
            target_url = config.target_http_url
        # 对HTTPS只能使用HTTPS代理，对HTTP只能使用HTTP代理
        resp = requests.get(target_url,
                            timeout=timeout,
                            proxies={
                                protocol: concat_proxy((protocol, ip, port))
                            },
                            headers={
                                'User-Agent': config.default_user_agent,
                            })
        return resp.status_code == 200
    except Exception:
        pass
    return False


def test_target_website():
    """
    这仅是一段测试代码，请忽略
    # 连续10次无代理请求，测试目标网站的响应速度
    # 这段代码是为了测算代理有效性的超时时间标准
    # 其它算无效代理IP(响应太慢，没有什么实用价值)
    :return:
    """
    begin = time.time()
    success_count = 0
    for _ in range(10):
        try:
            if requests.get(config.target_https_url).status_code == 200:
                success_count += 1
        except Exception as e:
            print(e)
    end = time.time()

    # 成功请求 10 次，总耗时 0.922 秒，平均单次请求耗时 0.092 秒
    print('成功请求 {} 次，总耗时 {:.3f} 秒，平均单次请求耗时 {:.3f} 秒'.
          format(success_count, end - begin, (end - begin) / 10))


if __name__ == '__main__':
    # test_target_website()

    # 本机出口IP：180.157.254.185

    # 速度有点慢，改用多线程试一下
    executor = ThreadPoolExecutor(max_workers=10)


    def test(item):
        flag, level = validate(*item)
        if flag:
            print(concat_proxy(item), level)
        # else:
        #     print(concat_proxy(item), '-' * 10)


    for item in get_all_proxies():
        executor.submit(test, item)

    executor.shutdown()

    # 查询前5页，一共5条有效代理IP？！完全没法用啊 ~
    print('完成全部有效代理IP检测')
