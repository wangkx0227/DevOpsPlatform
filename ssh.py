import paramiko  # https://docs.paramiko.org/en/stable/ 文档，实现ssh链接
import logging

# 配置日志
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='paramiko.log', filemode='w')



ssh = paramiko.SSHClient()  # 创建SSH客户端

ssh.set_log_channel("测试")

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 设置信任远程机器，允许连接不在known_hosts文件中的主机



ssh.connect(hostname='10.8.10.8', port=8000, username='cjl',password='123') # 连接到远程服务器


ssh.close()

