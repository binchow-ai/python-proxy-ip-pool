FROM python:3.7-alpine

# MAINTAINER ，镜像创建者
MAINTAINER zlikun <zlikun-dev@hotmail.com>

# 设置重新构建日期，当需要完整重新构建镜像时，可以修改该日期
ENV REBUILD_DATE 2017/09/25

# 先复制 requirements.txt 文件，避免其它文件修改导致重新构建镜像时，重复下载依赖库
ADD ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 通过环境变量配置Redis服务
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

# 将其它文件的复制放在安装依赖库之后
ADD ./ ./

# 将API服务集成在爬虫服务里了，所以暴露API服务的端口
EXPOSE 8888

ENTRYPOINT ["python", "main.py"]