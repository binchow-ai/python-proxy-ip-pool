# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq

# 实现一个爬虫，用于从：http://www.xicidaili.com/nn 上获取代理IP数据
# 默认只爬取前4页数据，可自行调整max_page参数来控制
max_page = 4
default_url = 'http://www.xicidaili.com/nn/'

# 生成爬虫目标URL列表
target_urls = [default_url + str(i) for i in range(1, max_page + 1)]

DEFAULT_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'


def get_proxies(url):
    """
    下载并解析目标网页中的代理数据
    :param url:
    :return:
    """
    try:
        # 下载代理列表页
        response = requests.get(url,
                                headers={
                                    'User-Agent': DEFAULT_UA,
                                    'Host': 'www.xicidaili.com',
                                })
        response.raise_for_status()
        html = response.text
        # 解析该页，获取全部代理IP及协议
        for tr in pq(html).find('tr:gt(0)'):
            tds = pq(tr).find('td')
            yield (tds[5].text.strip(), tds[1].text.strip(), tds[2].text.strip())
    except Exception as e:
        print(e)


def get_all_proxies():
    """
    获取全部代理数据
    :return:
    """
    for url in target_urls:
        yield from get_proxies(url)


if __name__ == '__main__':
    # 测试逻辑
    count = 1
    for proxy in get_all_proxies():
        print(proxy)
        count += 1

    print('一共获取到：{} 个代理IP'.format(count))
