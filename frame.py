import os
import urllib2
from const import SUPPORTED_FILE_TYPES

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


def get_hash(file_url):
    """
    Method that based on file url return appropriate hash.
    :param file_url: File that should be opened.
    :return: Hash for embedding Frame terminal.
    """
    file_extension = os.path.splitext(file_url)[1]
    if file_extension == SUPPORTED_FILE_TYPES[0]:
        return HASH_NOTEPAD
    else:
        return HASH_PAINT
