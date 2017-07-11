"""
To run:
    (from this directory)
    install requirements:
        make sure you have a python 2 or 3 runtime
        $ pip install -r requirements.txt
    run flask server:
        $ python -m flask_example
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/chat/messages', methods=['POST'])
def messages():
    print("Recieved Form from Lessenger UI:%s" % request.form)

    response = jsonify()
    # set CORS wildcard header
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
