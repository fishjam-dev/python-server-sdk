from flask import Flask, request, Response
from jellyfish import Notifier

app = Flask(__name__)
data_queue = None

@app.route('/webhook', methods=['POST'])
def respond_root():
    json = request.get_json()
    json = Notifier.handle_json(json)
    data_queue.put(json)

    return Response(status=200)


def run_server(queue):
    global data_queue
    data_queue = queue
    app.run(port=5000, host="0.0.0.0", use_reloader=False,debug=False, threaded=True)