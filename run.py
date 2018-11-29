from flask import Flask, request, jsonify
from flask_api import status
from src.calc import mapping
from src.errors import InvalidUsage, get_http_exception_handler

app = Flask(__name__)


def mapper(action, a, b):
    func = mapping.get(action)
    try:
        return func(a, b)
    except ZeroDivisionError:
        raise InvalidUsage("ZeroDivision not supported")


def calc(req):
    method, a, b = all_params = req.get("method"), req.get("a"), req.get("b")
    if None in all_params:
        raise InvalidUsage("check you params")
    if isinstance(a, str) or isinstance(b, str):
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            raise InvalidUsage("check you params")
    return {"result": mapper(method, a, b)}, status.HTTP_200_OK


@app.route('/resource', methods=['POST', "GET"])
def hello():
    if request.method == 'POST':
        response, resp_status = calc(request.get_json())
    elif request.method == "GET":
        body = request.get_json()
        if bool(body):
            response, resp_status = calc(body)
            response.update({"message": "you are hackerman =)"})
        else:
            response, resp_status = calc(request.args)
    else:
        raise InvalidUsage("request method is not supported")

    return jsonify(response), resp_status


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.handle_http_exception = get_http_exception_handler(app)
    app.run(host="192.168.88.195", port=5000)
