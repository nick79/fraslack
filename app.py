import sys
from flask import Flask
from flask import Response
from flask import logging
from flask import render_template
from flask import request
from flask import send_from_directory
from itsdangerous import BadSignature, Signer
from const import FRAME_PATH, SLACK_PATH, DATA_PATH, SUPPORTED_FILE_TYPES
from frame import file_exist, get_hash
from globals import SECRET_KEY, PORT, HASHES
from slack import validate, process_command

app = Flask(__name__, static_url_path='/static')
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route for starting (index) page.
    :return: Index page of application.
    """
    return render_template('index.html')


@app.route(DATA_PATH)
def send_data(path):
    """
    Route for serving static data required for testing purpose.
    :param path: Name of static file that should be opened.
    :return: Static file.
    """
    return send_from_directory('static', path)


@app.route(SLACK_PATH, methods=['POST'])
def slack():
    """
    Route for handling custom slack command.
    :return: Link with embedded Frame terminal or in case of not valid slack token Unauthorized response.
    """
    text, token = extract_slack_request()
    if validate(token):
        response_message = process_command(text)
        return Response(response_message), 200
    else:
        return Response(), 401


def extract_slack_request():
    """
    Helper method that extract necessary parameters from Request received from Slack.
    :return: URL of file that should be opened and slack token.
    """
    token = request.form.get('token')
    text = request.form.get('text')
    channel = request.form.get('channel_name')
    user = request.form.get('user_name')
    app.logger.info('User: %s  in channel: %s requested file: %s', str(user), str(channel), str(text))
    return text, token


@app.route(FRAME_PATH)
def frame():
    """
    Route for providing embedded Frame terminal with opened file.
    :return: Web page with embedded Frame terminal or in case of bad link Error page with coresponding message.
    """
    signer = Signer(SECRET_KEY)
    try:
        file_url = signer.unsign(request.args.get('file_url'))
        if file_exist(file_url):
            app.logger.info('Opened file %s', str(file_url))
            hash_id = get_hash(file_url)
            return render_template('frame.html', hash=hash_id, file=file_url)
        else:
            message = 'File: %s does not exist' % (str(file_url))
            app.logger.warn(message)
            return render_template('error.html', error_message=message)
    except BadSignature as e:
        app.logger.error(e)
        return render_template('error.html', error_message='Bad signature in link')


def validate_hashes():
    if all(hash in HASHES for hash in SUPPORTED_FILE_TYPES):
        return True
    else:
        app.logger.error('Wrong configuration - hashes for some applications are missing!')


if __name__ == '__main__':
    if validate_hashes():
        app.run(debug=True)
        app.run(host='0.0.0.0', port=PORT)
    else:
        sys.exit(1)
