# Predefined Slack messages
HELP_MESSAGE = 'To open file at [file_url] address within Frame platform please use `/frame file_url`.'
UNSUPPORTED_MESSAGE = 'Unsupported File Type'
UNSUPPORTED_PROTOCOL_MESSAGE = 'File address must start with http:// or https://'

# Supported file types
SUPPORTED_FILE_TYPES = ['.txt', '.jpg']

# Protocols
PROTOCOLS = ('http://', 'https://')

# Routes
BASE_PATH = 'https://fraslack.herokuapp.com'
FRAME_PATH = '/frame'
SLACK_PATH = '/slack'
DATA_PATH = '/data/<path:path>'
