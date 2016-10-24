import urllib2


def file_exist(file_url):
    """
    Method that check if file at provided url exist.
    :param file_url: Url of the file that should be checked.
    :return: True if file exist, otherwise False.
    """
    request = urllib2.Request(file_url)
    request.get_method = lambda : 'HEAD'
    try:
        response = urllib2.urlopen(request)
        return True
    except urllib2.HTTPError:
        return False