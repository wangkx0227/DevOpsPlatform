# 1.SSH链接

## 1.`SSHClient`基本使用

```python
import paramiko  # https://docs.paramiko.org/en/stable/ 文档，实现ssh链接


ssh = paramiko.SSHClient()  # 创建SSH客户端
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 设置信任远程机器，允许连接不在known_hosts文件中的主机
"""
    paramiko.AutoAddPolicy()
    AutoAddPolicy 自动添加主机名及主机密钥到本地HostKeys对象，不依赖load_system_host_key的配置。即新建立ssh连接时不需要再输入yes或no进行确认
    WarningPolicy 用于记录一个未知的主机密钥的python警告。并接受，功能上和AutoAddPolicy类似，但是会提示是新连接
    RejectPolicy 自动拒绝未知的主机名和密钥，依赖load_system_host_key的配置。此为默认选项
"""
ssh.connect(hostname='10.8.10.8', port=8000, username='cjl', password='123') # 连接到远程服务器
"""
    hostname：连接的目标主机
    port：目标主机的端口
    username：验证的用户可以为None
    password：验证的密码可以为None
    pkey：私钥的验证方式可以为None
    key_filename：一个文件名或者一个文件列表，指定私钥文件
    timeout：TCP连接的超时时间，可以为None
    allow_agent：是否允许连接到ssh代理，默认为True
    look_for_keys：是否在~/.ssh中搜索秘钥文件，默认为True
    compress：是否打开压缩，默认False
"""

stdin, stdout, stderr = ssh.exec_command("free -h") # 执行命令，并且返回错误信息正确信息
"""
    exec_command 执行远程的ssh命令
    timeout 设置超时时间
    get_pty 从服务端请求一个伪终端（bool）
"""
sftp = ssh.open_sftp()
"""
    open_sftp 在当前ssh会话上建立一个ftp对象，返回一个sftpclient对象，可以通过对象进行下载或者上传
"""

result = stdout.read() + stderr.read()
"""
    输出内容
"""
print(result.decode())

ssh.close()
"""
    关闭链接
"""


ssh.connect链接方式：
	是一个更高级的接口，它封装了 Transport，提供了更简单的方法来进行SSH连接和管理。
    它自动处理连接的建立和关闭，简化了会话（session）的管理。
    还有一些额外的功能，如主机密钥管理、知道主机密钥策略等。进行了代码简化。
```

## 2.`Transport` 底层类链接

```python
import paramiko  # https://docs.paramiko.org/en/stable/ 文档，实现ssh链接

 
# 创建一个通道
transport = paramiko.Transport(('10.8.10.8', 8000))
transport.connect(username='cjl', password='123')
 
 # 打开一个会话来执行命令
session = transport.open_session()
if session.active:
    session.exec_command('df -h')
    while True:
        data = session.recv(1024) # 最大接受1024kb，超出循环获取
        if not data:
            break
        print(data.decode()) # 打印结果
 
# 关闭连接
transport.close()

作用：
    建立连接：Transport 负责初始化与远程服务器的网络连接。它使用SSH协议与远程服务器建立安全的连接。
    认证：在连接建立后，Transport 负责处理身份验证过程。这可以通过密码、SSH密钥或GSSAPI等方法进行。
    加密：Transport 确保所有传输的数据都是加密的，以保护数据免受窃听和篡改。
    多路复用：Transport 支持在单个SSH连接上创建多个通道（channels），这允许同时执行多个操作，如执行命令、传输文件等。
    心跳检测：Transport 可以配置心跳检测机制，以确保连接的活跃状态，并在连接超时自动重新连接。
    异常处理：Transport 会捕获并处理SSH连接过程中可能出现的异常，如网络中断、认证失败等。
    关闭连接：Transport 提供方法来优雅地关闭连接，释放资源。
# 可以灵活地控制SSH连接的各个方面，包括连接建立、身份验证、数据传输和连接关闭等。适合需要对SSH连接进行精细控制的场景，或者需要实现一些特殊功能的高级用法
```

## 3.密钥链接-SSHClient

```python
# 前提：需要先将密钥发送到远程端

import paramiko
 
# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file(r'C:\\Users\\Administrator\\.ssh\\id_rsa')
  
#实例化SSHClient
client = paramiko.SSHClient()
  
#自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
#连接SSH服务端，以用户名和密钥进行认证
client.connect(hostname='10.8.10.8', port=8000, username='cjl',pkey=private)
 
# 打开一个Channel并执行命令
stdin, stdout, stderr = client.exec_command('df -h ')
# stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
  
# 打印执行结果
print(stdout.read().decode('utf-8'))
  
# 关闭SSHClient
client.close()
```

## 4.密钥链接-Transport

```python
import paramiko
 
# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file(r'C:\\Users\\Administrator\\.ssh\\id_rsa')
  
# 创建一个通道
transport = paramiko.Transport(('10.8.10.8', 8000))
transport.connect(username='cjl', pkey=private)  # 使用密钥
 
 # 打开一个会话来执行命令
session = transport.open_session()
if session.active:
    session.exec_command('df -h')
    while True:
        data = session.recv(1024) # 最大接受1024kb，超出循环获取
        if not data:
            break
        print(data.decode()) # 打印结果
 
# 关闭连接
transport.close()
```

# 2.SFTP链接

```bash
SFTPCLient作为一个sftp的客户端对象，根据ssh传输协议的sftp会话，实现远程文件操作，如上传、下载、权限、状态
  
from_transport(cls,t) 创建一个已连通的SFTP客户端通道
put(localpath, remotepath, callback=None, confirm=True) 将本地文件上传到服务器 参数confirm：是否调用stat()方法检查文件状态，返回ls -l的结果
get(remotepath, localpath, callback=None) 从服务器下载文件到本地
mkdir() 在服务器上创建目录
remove() 在服务器上删除目录
rename() 在服务器上重命名目录
stat() 查看服务器文件状态
listdir() 列出服务器目录下的文
```

## 1.上传功能-Transport-put

```python
import paramiko
 
# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file(r'C:\\Users\\Administrator\\.ssh\\id_rsa')
  
# 创建一个通道
transport = paramiko.Transport(('10.8.10.8', 8000))
transport.connect(username='cjl', pkey=private)  # 使用密钥
 
 # 创建ftp客户端
sftp = paramiko.SFTPClient.from_transport(transport)
localpath = "./1.txt" # 宿主机的文件
remotepath = "/tmp/1.txt" # 上传到服务器的位置以及名称

sftp.put(localpath, remotepath)
# 关闭sftp链接
sftp.close()
# 关闭连接
transport.close()
```

## 2.上传功能-SSHClient-put

```python
import paramiko


ssh = paramiko.SSHClient()  # 创建SSH客户端
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 设置信任远程机器，允许连接不在known_hosts文件中的主机
ssh.connect(hostname='10.8.10.8', port=8000, username='cjl', password='123') # 连接到远程服务器
sftp = ssh.open_sftp()

localpath = "./1.txt" # 宿主机的文件
remotepath = "/tmp/2.txt" # 上传到服务器的位置以及名称

sftp.put(localpath, remotepath)

# 关闭链接
sftp.close()
ssh.close()
```

## 3.下载功能-get

```python
# 无法进行下载整个目录。只能通过递归方式进行下载

import paramiko  # https://docs.paramiko.org/en/stable/ 文档，实现ssh链接


ssh = paramiko.SSHClient()  # 创建SSH客户端
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 设置信任远程机器，允许连接不在known_hosts文件中的主机
ssh.connect(hostname='10.8.10.8', port=8000, username='cjl', password='123') # 连接到远程服务器
sftp = ssh.open_sftp()

# 远程文件路径
remote_path_file = "/etc/passwd" # 远程的文件
local_path = "./passwd.txt" # 下载本地的位置

# 下载文件
sftp.get(remote_path_file, local_path)

# 关闭链接
sftp.close()
ssh.close()
```

## 4.除了上传的其他操作

```python
import paramiko  # https://docs.paramiko.org/en/stable/ 文档，实现ssh链接


ssh = paramiko.SSHClient()  # 创建SSH客户端
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 设置信任远程机器，允许连接不在known_hosts文件中的主机
ssh.connect(hostname='10.8.10.8', port=8000, username='cjl', password='123') # 连接到远程服务器
sftp = ssh.open_sftp()

# 创建目录
	sftp.mkdir('new_directory') # 可以能会出现权限不足的情况，普通用户

# 列出当前目录内容下的文件或者目录
	files = sftp.listdir('./')

# 删除目录
	sftp.rmdir('new_directory')

# 检查文件状态/获取路径信息 stat与lstat性质相同
    import stat # 通过当前模块可以判断是文件还是文件夹
    file_status = sftp.stat('/etc/passwd')
    path_status = sftp.lstat('/tmp')
    if stat.S_ISDIR(path_status.st_mode):
         print('文件夹')
    else:
         print("文件")

# 修改文件名称
    old_name = '/tmp/1.txt' # 旧
    new_name = '/tmp/111.txt' # 新
    sftp.rename(old_name,new_name)

# 删除文件
	sftp.remove('/tmp/2.txt') # 无文件，报错

# 创建软连接
	sftp.symlink('/tmp/','/tmp/123')

# 设置权限
    remote_file_path = '/tmp/111.txt'
    new_permissions = 0o777  # 设置权限为 644，即 -rw-r--r--
    sftp.chmod(remote_file_path, new_permissions)

# 设置文件的用户组与用户（用户组id和用户id，普通用户需要提权）
    remote_file_path = '/tmp/111.txt'
    uid = 1
    gid = 1
    sftp.chown(remote_file_path, uid,gid)

# 读取软连接链接的真实路径
	read_link = sftp.readlink('/tmp/123')

# 修改当前sftp的工作目录（默认是None，没有工作目录，当使用getcwd时返回内容为None）
	sftp.chdir('/tmp/')

# 查看当前的工作目录
    cwd = sftp.getcwd()
    print(cwd)
    
# 关闭链接
sftp.close()
ssh.close()
```

# sshclient类

```bash
import paramiko  # https://docs.paramiko.org/en/stable/ 文档，实现ssh链接
import logging

# 配置日志
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='paramiko.log', filemode='w')



ssh = paramiko.SSHClient()  # 创建SSH客户端
# 1.设置日志通道名称[日志名称]（可选）, 当前代码需要在链接放在链接之前.否则设置就会失败.
# ssh.set_log_channel("测试")

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 设置信任远程机器，允许连接不在known_hosts文件中的主机

# 2.自动加载系统默认的 known_hosts 文件，(其他机器公钥，已经免密过了)。
# filename='密钥文件' 默认：~/.ssh/known_hosts，免密操作的一部分
# ssh.load_system_host_keys() 

# 3.主动加载known_hosts(其他机器公钥，已经免密过了)。注意主动加载需要注意路径
# ssh.load_host_keys(filename=r'C:\\Users\\Administrator\\.ssh\\known_hosts')

ssh.connect(hostname='10.8.10.8', port=8000, username='cjl',password='123') # 连接到远程服务器


# 4.将远程主机密钥保存到文件中，注意只在输入密码的情况下，才会有内容。在开发环境中测试，可以使用 AutoAddPolicy 自动添加主机密钥，但在生产环境中，建议手动管理主机密钥。
# ssh.save_host_keys('./1.txt')

# 5.获取当前加载的主机密钥（远程）可以更灵活地管理和验证主机密钥，从而确保 SSH 连接的安全性。同时也可以主动添加密钥。
# host_keys = ssh.get_host_keys()
# for hostname in host_keys:
#     print(f"Host: {hostname}")
#     for keytype in host_keys[hostname]:
#         print(f"  Key Type: {keytype}")
#         print(f"  Key: {host_keys[hostname][keytype]}")
# host_keys.add(hostname, 'ssh-rsa', paramiko.RSAKey.from_private_key_file('path/to/public_key')) # 手动添加密钥


# 6.返回一个sftp对象
# sf = ssh.open_sftp()
# 7.返回此SSH连接的基础传输对象。这可以用于执行较低级别的任务，例如打开特定类型的通道。 也就是底层对象 Transport 类型
# t = ssh.get_transport()



#8.开启一个伪终端进行交互
# 启动交互式 shell 会话
# shell = ssh.invoke_shell(term='xterm', width=120, height=40)

# # 等待终端提示符出现
# while True:
#     if shell.recv_ready():
#         output = shell.recv(1024).decode('utf-8')
#         print(output, end='')
#         if 'cjl@cjl:' in output:  # 等待提示符出现
#             break

# # 发送命令
# shell.send('free -h')

# # 等待命令输出
# while True:
#     if shell.recv_ready():
#         output = shell.recv(1024).decode('utf-8')
#         print(output, end='')
#         if '$' in output:  # 等待提示符出现
#             break

ssh.close()


```

