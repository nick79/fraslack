import os
from flask import Flask
from flask import Response
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import url_for
from itsdangerous import TimestampSigner, BadTimeSignature, BadSignature, SignatureExpired
from const import FRAME_PATH, SLACK_PATH, DATA_PATH, SECRET_KEY, LINK_DURATION
from slack import validate, process_command

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route(DATA_PATH)
def send_data(path):
    return send_from_directory('static', path)


@app.route(SLACK_PATH, methods=['POST'])
def slack():
    if validate(request):
        response_message = process_command(request.form.get('text'))
        return Response(response_message), 200


@app.route(FRAME_PATH)
def frame():
    signer = TimestampSigner(SECRET_KEY)
    try:
        file_url = signer.unsign(request.args.get('file_url'), max_age=LINK_DURATION)
        return render_template('frame.html', file=file_url)
    except (BadSignature, BadTimeSignature, SignatureExpired) as e:
        print e
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
