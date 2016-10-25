# Supported file types
SUPPORTED_FILE_TYPES = ['.txt', '.jpg']
UNSUPPORTED_MESSAGE = 'Unsupported File Type'

# Protocols
PROTOCOLS = ('http://', 'https://')
UNSUPPORTED_PROTOCOL = 'File address must start with http:// or https://'

# Routes
BASE_PATH = 'https://fraslack.herokuapp.com'
FRAME_PATH = '/frame'
SLACK_PATH = '/slack'
DATA_PATH = '/data/<path:path>'

# Embedded Frame terminal
FRAME_SCRIPT = "<script src='http://app.fra.me/embed/mf2ea.js?hash=%s&size=L&file =%s&autostart=true'></script>"
