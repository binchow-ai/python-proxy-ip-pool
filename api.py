# -*- coding: utf-8 -*-

import redis
from flask import Flask, jsonify

import config
from process import DataProcessor

app = Flask(__name__)
dp = DataProcessor()

client = redis.StrictRedis(host=config.redis_host,
                           port=config.redis_port,
                           decode_responses=True,
                           charset='utf-8')


@app.route('/')
def index():
    return 'OK'


@app.route('/<protocol>/random')
def random(protocol):
    """
    随机返回一个优质代理IP
    :param protocol:
    :return:
    """
    return client.srandmember('{}:proxies:{}'.format(protocol, 1))


@app.route('/proxies')
def proxies():
    """
    返回全部代理IP
    :return:
    """
    return jsonify([proxy for proxy, _ in dp.query()])


@app.route('/<protocol>/proxies')
def proxies_by_protocol(protocol):
    """
    选择符合指定协议的全部代理IP
    :param protocol:
    :return:
    """
    return jsonify([proxy for proxy, _ in dp.query()
                    if proxy.startswith('{}://'.format(protocol))])


def run_api_server():
    """
    启动API服务
    :return:
    """
    app.run(host="0.0.0.0", port=8888)


if __name__ == '__main__':
    run_api_server()
