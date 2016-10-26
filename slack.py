import os
from itsdangerous import Signer
import globals
from const import SUPPORTED_FILE_TYPES, FRAME_PATH, BASE_PATH, UNSUPPORTED_MESSAGE, PROTOCOLS, \
    UNSUPPORTED_PROTOCOL_MESSAGE, HELP_MESSAGE


def validate(token):
    """
    Method that validate passed Slack token.
    :param token: Slack token that should be validated.
    :return: True if validation is successful, otherwise False.
    """
    if token == globals.SLACK_TOKEN:
        return True
    return False


def is_file_type_supported(file_url):
    """
    Method that determine if file type is supported.
    :param file_url: Url of the file that should be opened.
    :return: True in case of supported file, otherwise False.
    """
    file_extension = os.path.splitext(file_url)[1]
    if file_extension in SUPPORTED_FILE_TYPES:
        return True
    return False


def create_url(text):
    """
    Method that create signed link that should be send it to Slack.
    :param text: Url of the file that should be opened.
    :return: Signed link for opening file within embedded Frame terminal.
    """
    signer = Signer(globals.SECRET_KEY)
    url = BASE_PATH + FRAME_PATH + '?file_url=' + signer.sign(text)
    return url


def process_command(text):
    """
    Method first check if user provided any file url or if he typed help, and in that case return short help message
    about command usage. If url is complete and type of requested file from Slack is supported method in that case
    create link for opening it.
    :param text: Received url of file from slack.
    :return: Help message or link for opening file in case that file is supported, otherwise message about unsupported
    file.
    """
    if not text or text.startswith('help'):
        return HELP_MESSAGE
    elif not text.startswith(PROTOCOLS):
        return UNSUPPORTED_PROTOCOL_MESSAGE
    elif is_file_type_supported(text):
        return create_url(text)
    else:
        return UNSUPPORTED_MESSAGE
