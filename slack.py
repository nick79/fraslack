import os
from const import SLACK_TOKEN, SUPPORTED_FILE_TYPES


def validate(request):
    if request.form.get('token') == SLACK_TOKEN:
        return True
    return False


def is_file_type_supported(file_url):
    file_extension = os.path.splitext(file_url)[1]
    if file_extension in SUPPORTED_FILE_TYPES:
        return True
    return False


def process_command(request):
    text = request.form.get('text')
    if is_file_type_supported(text):
        return 'File Type is supported'
    return 'Unsupported File Type'
