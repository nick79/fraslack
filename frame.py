import os
import urllib2
from const import FRAME_SCRIPT, SUPPORTED_FILE_TYPES

HASH_NOTEPAD = str(os.environ.get("HASH_NOTEPAD"))
HASH_PAINT = str(os.environ.get("HASH_PAINT"))


def file_exist(file_url):
    """
    Method that check if file at provided url exist.
    :param file_url: Url of the file that should be checked.
    :return: True if file exist, otherwise False.
    """
    request = urllib2.Request(file_url)
    request.get_method = lambda: 'HEAD'
    try:
        response = urllib2.urlopen(request)
        return True
    except urllib2.HTTPError:
        return False


def generate_frame_script(file_url):
    """
    Method that based on file url generate javascript necessary for embedding Frame terminal.
    :param file_url: File that should be opened.
    :return: Generated javascript,
    """
    file_extension = os.path.splitext(file_url)[1]
    if file_extension == SUPPORTED_FILE_TYPES[0]:
        hash_id = HASH_NOTEPAD
    else:
        hash_id = HASH_PAINT
    return FRAME_SCRIPT % (str(hash_id), str(file_url))
