import psutil
from datetime import datetime
from flask import Flask, jsonify
from devops_app.utilits import logger
from devops_app.settings import VERSION

app = Flask(__file__)


@app.route('/')
def index():
    logger.info("访问日志！")
    return 'Hello, world!'


@app.route('/healthcheck')
def health_check():
    """
    健康检查路由
    版本信息：
    应用程序的版本号可以帮助你了解正在运行的代码版本。
    启动时间：
    显示应用程序启动的时间戳，有助于了解应用的运行时间。
    负载信息：
    当前系统的负载信息，如CPU和内存使用率。
    数据库连接状态：
    如果应用程序依赖数据库，检查数据库连接是否正常。
    缓存状态：
    如果使用了缓存系统，检查缓存是否正常工作。
    依赖服务状态：
    如果应用程序依赖外部服务（如API、消息队列等），检查这些服务的健康状况。
    错误计数：
    应用程序启动以来遇到的错误数量。
    请求计数：
    应用程序处理的请求总数。
    系统资源：
    如磁盘空间、网络连接状态等。
    配置检查：
    验证关键配置项是否正确。
    安全状态：
    如SSL证书的有效性。
    自定义指标：
    根据业务需求定义的任何其他关键性能指标（KPIs）
    :return:
    """
    uptime = datetime.now() - app.config['START_TIME']
    health_info = {
        "status": "up",
        "version": VERSION,  # 版本
        "uptime": uptime.days,  # 启动天数
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "database_status": "connected",  # 假设数据库连接正常
        # 添加其他健康检查项...
    }
    return jsonify(health_info)


if __name__ == '__main__':
    app.config['START_TIME'] = datetime.now()
    app.run(debug=True)
