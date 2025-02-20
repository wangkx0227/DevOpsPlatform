from core import app
from core.utilits import send_email
from core.settings import ApiResponse


@app.route("/")
def index():
    return "测试"


@app.route('/example', methods=['GET'])
def example():
    # 成功响应
    send_email("我是标题", "it-19@1bizmail.com", "我是主题")
    return ApiResponse.success(data={"key": "value"}, message="Request processed successfully")


@app.route('/error', methods=['GET'])
def error_example():
    # 错误响应
    return ApiResponse.error(message="Invalid request", status=400)


if __name__ == '__main__':
    print(app.url_map)
    app.run(host="127.0.0.1", port=8080)
