# 测试代码，请忽略
import os
import re

# 拆解URL测试
url = 'http://118.190.95.43:9001'
# ('http', '118.190.95.43', '9001')
print(tuple(re.split(r'(://|:)', url)[::2]))
# http 118.190.95.43 9001
print(*tuple(re.split(r'(://|:)', url)[::2]))
# http 118.190.95.43 9001
print(*re.split(r'(://|:)', url)[::2])


def log(protocol, ip, port):
    print('protocol = {}, ip = {}, port = {}'.format(protocol, ip, port))


# 测试解包对传参的影响
log(*re.split(r'(://|:)', url)[::2])

# 测试获取环境变量(为Docker化配置做准备)
print(os.environ.get('PATH'))
print(os.environ.get('REDIS_PORT', 6379))
