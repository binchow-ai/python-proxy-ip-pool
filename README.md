# 动态代理IP池

通过定时抓取[西刺代理](http://www.xicidaili.com/)的代理IP数据，并定时验证IP有效性来实现一个动态代理IP池

## 用法
> 运行 `main.py` 即可

## Docker
```
# 使用Dockerfile构建Docker镜像
$ docker build -t proxy-ip-pool .

# 测试镜像(使用临时容器)
$ docker run --rm -p 8888:8888 \
--env REDIS_HOST=192.168.0.105 \
proxy-ip-pool

# 启动容器后，通过访问 http://localhost:8888/ 来确认容器是否正常
# 正常访问成功后返回 OK

# 如果访问的Redis服务也是一个Docker容器，可以通过 --link redis 来连接
$ docker run --rm \
-p 8888:8888 \
--link redis \
proxy-ip-pool
```
