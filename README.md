# 动态代理IP池

通过定时抓取[西刺代理](http://www.xicidaili.com/)的代理IP数据，并定时验证IP有效性来实现一个动态代理IP池

## 用法
> 运行 `main.py` 即可

## Docker
```
# 下载镜像
$ docker pull zlikun/proxy-ip-pool

# 启动容器，依赖redis服务
# 如果redis非docker，可以使用 --env REDIS_HOST=127.0.0.1 方式来实现)
$ docker run -d \
--name proxy-ip-pool \
-p 8888:8888 \
--restart always \
--link redis \
zlikun/proxy-ip-pool

$ docker container ls | grep proxy
4e8e53c9f9f2        zlikun/proxy-ip-pool   "python main.py"         13 minutes ago      Up 13 minutes       0.0.0.0:8888->8888/tcp     proxy-ip-pool
```

## API
- 检查服务
```
$ curl -i localhost:8888/
OK
```
- 随机获取一个代理IP(区分HTTP和HTTPS协议)
```
$ curl localhost:8888/http/random
http://118.190.95.43:9001

$ curl localhost:8888/https/random   
https://118.31.220.3:8080
```
- 获取全部代理IP(区分HTTP和HTTPS协议)
```
$ curl localhost:8888/http/proxies 
["http://118.190.95.43:9001","http://118.190.95.35:9001","http://61.135.217.7:80"]

$ curl localhost:8888/https/proxies
["https://118.31.220.3:8080","https://221.228.17.172:8181"]
```

## 仅供测试
[随机获取一个HTTPS代理IP](https://api.zlikun.com/https/random)


吐槽一下，免费的代理IP质量大都很差，整个西刺前4页几百个IP有效的不超过10个 。。。