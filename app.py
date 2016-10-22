import os
from flask import Flask
from flask import Response
from flask import render_template
from flask import request
from flask import send_from_directory

SLACK_TOKEN = 'LxqD74GgYpSCmQlNsl5MXckS'

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('hello.html')


@app.route('/data/<path:path>')
def send_data(path):
    return send_from_directory('static', path)


@app.route('/slack', methods=['POST'])
def slack():
    if request.form.get('token') == SLACK_TOKEN:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response('Milan Test'), 200


if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
