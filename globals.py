import os
from envparse import env

SLACK_TOKEN = str(os.environ.get("SLACK_TOKEN"))
SECRET_KEY = str(os.environ.get("SECRET_KEY"))
HASHES = env.dict('HASHES')
PORT = int(os.environ.get("PORT", 5000))
HASH_NOTEPAD = str(os.environ.get("HASH_NOTEPAD"))
HASH_PAINT = str(os.environ.get("HASH_PAINT"))