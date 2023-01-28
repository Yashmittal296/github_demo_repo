import json

import flask
from flask import Flask
import SandBox as sm

app = Flask(__name__)


@app.route('/yash', methods=['POST'])
def get_sum():
    json_input = flask.request.data.decode('utf-8')
    dict_input = json.loads(json_input)
    a = dict_input['a']
    b = dict_input['b']
    Obj_Sm = sm.Sum()
    result = Obj_Sm.get_sum(a, b)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
