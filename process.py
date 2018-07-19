# -*- coding: utf-8 -*-

import config
import redis


# 数据持久化模块，用于将代理IP数据写入数据库(Mongo) / 缓存(Redis)
# 本案采用Redis，Mongo有兴趣的可以自行实现
# 数据库采用List数据结构实现，不过用Redis的话，原始数据库中标记无效数据就无法实现了
# 但这个并不是很重要，原始数据库中只记录无效数据即可


class DataProcess(object):

    def __init__(self):
        self.client = redis.StrictRedis(host=config.redis_host,
                                        port=config.redis_port,
                                        decode_responses=True,
                                        charset='utf-8')

    def cache(self, proxies):
        """
        缓存无效代理IP数据，缓存时间默认24H
        :param proxies:
        :return:
        """
        pass

    def save(self, proxies):
        """
        保存有效代理IP数据
        :param proxies:
        :return:
        """
        pass

    def remove(self, proxies):
        """
        清除有效IP数据库中的数据
        :param proxies:
        :return:
        """
        pass
