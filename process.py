# -*- coding: utf-8 -*-

import redis

import config


class DataProcessor(object):

    def __init__(self):
        self._client = redis.StrictRedis(host=config.redis_host,
                                         port=config.redis_port,
                                         decode_responses=True,
                                         charset='utf-8')

    def query(self):
        """
        取出全部代理IP数据
        :return:
        """
        yield from [(proxy, 1) for proxy in self._client.smembers('http:proxies:1')]
        yield from [(proxy, 0) for proxy in self._client.smembers('http:proxies:0')]
        yield from [(proxy, 1) for proxy in self._client.smembers('https:proxies:1')]
        yield from [(proxy, 0) for proxy in self._client.smembers('https:proxies:0')]

    def save(self, proxy, level):
        """
        保存代理IP
        :param proxy:
        :param level:
        :return:
        """
        key = self._get_key(proxy, level)
        self._client.sadd(key, proxy)

    def remove(self, proxy, level):
        """
        删除代理IP
        :param proxy:
        :param level:
        :return:
        """
        key = self._get_key(proxy, level)
        self._client.srem(key, proxy)

    def _get_key(self, proxy, level):
        """
        根据代理IP信息，返回缓存键
        :param proxy:
        :return:
        """
        if proxy.startswith('http://'):
            return 'http:proxies:{}'.format(level)
        else:
            return 'https:proxies:{}'.format(level)


if __name__ == '__main__':
    """
    测试代码
    """

    dp = DataProcessor()

    dp.save('http://118.190.95.43:9001', 1)
    dp.save('https://118.31.220.3:8080', 0)

    print('第一组查询：')
    # http://118.190.95.43:9001 1
    # https://118.31.220.3:8080 0
    for proxy, level in dp.query():
        print(proxy, level)

    dp.remove('https://118.31.220.3:8080', 0)

    print('第二组查询：')
    # http://118.190.95.43:9001 1
    for proxy, level in dp.query():
        print(proxy, level)
