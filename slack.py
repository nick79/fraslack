import os
from itsdangerous import TimestampSigner
from const import SLACK_TOKEN, SUPPORTED_FILE_TYPES, FRAME_PATH, BASE_PATH, UNSUPPORTED_MESSAGE, SECRET_KEY


def validate(token):
    if token == SLACK_TOKEN:
        return True
    return False


def is_file_type_supported(file_url):
    file_extension = os.path.splitext(file_url)[1]
    if file_extension in SUPPORTED_FILE_TYPES:
        return True
    return False


def create_url(text):
    signer = TimestampSigner(SECRET_KEY)
    url = BASE_PATH + FRAME_PATH + '?file_url=' + signer.sign(text)
    return url


def process_command(text):
    if is_file_type_supported(text):
        return create_url(text)
    return UNSUPPORTED_MESSAGE

