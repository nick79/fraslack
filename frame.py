import os
import requests
from requests import ConnectionError
from globals import HASHES


def file_exist(file_url):
    """
    Method that check if file at provided url exist.
    :param file_url: Url of the file that should be checked.
    :return: True if file exist, otherwise False.
    """
    try:
        response = requests.head(file_url)
        if 200 <= response.status_code < 300:
            return True
        return False
    except ConnectionError:
        return False


def get_hash(file_url):
    """
    Method that based on file url return appropriate hash.
    :param file_url: File that should be opened.
    :return: Hash for embedding Frame terminal.
    """
    file_extension = os.path.splitext(file_url)[1]
    return str(HASHES.get(file_extension))
