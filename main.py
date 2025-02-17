from devops_app import app
from devops_app.settings import ApiResponse


@app.route("/")
def index():
    return "测试"


@app.route('/example', methods=['GET'])
def example():
    # 成功响应
    print()
    return ApiResponse.success(data={"key": "value"}, message="Request processed successfully")


@app.route('/error', methods=['GET'])
def error_example():
    # 错误响应
    return ApiResponse.error(message="Invalid request", status=400)


if __name__ == '__main__':
    print(app.url_map)
    app.run(host="0.0.0.0")
