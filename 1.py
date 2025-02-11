# server.py
import asyncio
import websockets
import paramiko # https://docs.paramiko.org/en/stable/ 文档，实现ssh链接

async def handle_connection(websocket, path):
    async for message in websocket:
        if message.startswith("ssh:"):
            _, ssh_command = message.split(":", 1)
            try:
                # 创建 SSH 客户端
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('hostname', username='username', password='password')

                # 执行命令
                stdin, stdout, stderr = ssh.exec_command(ssh_command)
                result = stdout.read() + stderr.read()

                # 关闭连接
                ssh.close()

                # 发送结果回 WebSocket 客户端
                await websocket.send(result.decode())
            except Exception as e:
                await websocket.send(str(e))


# start_server = websockets.serve(handle_connection, "localhost", 8765)
# 
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.8.10.8', port=8000, username='cjl', password='123')
stdin, stdout, stderr = ssh.exec_command("pwd")
result = stdout.read() + stderr.read()
print(result.decode())
ssh.close()

