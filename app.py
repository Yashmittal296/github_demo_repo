import json

from flask import Flask, request
import SandBox as Sb

app = Flask(__name__)


@app.route('/yash', methods=['POST'])
def get_sum():
    json_input = request.data.decode('utf-8')
    dict_input = json.loads(json_input)
    a = dict_input['a']
    b = dict_input['b']
    objSb = Sb.Sum()
    result = objSb.get_sum(a, b)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
