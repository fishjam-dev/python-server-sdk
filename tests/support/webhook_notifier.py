# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring, global-statement

from flask import Flask, request, Response
from jellyfish import Notifier

app = Flask(__name__)
DATA_QUEUE = None

@app.route('/webhook', methods=['POST'])
def respond_root():
    json = request.get_json()
    json = Notifier.handle_json(json)
    DATA_QUEUE.put(json)

    return Response(status=200)


def run_server(queue):
    global DATA_QUEUE
    DATA_QUEUE = queue
    app.run(port=5000, host="0.0.0.0", use_reloader=False,debug=False, threaded=True)
