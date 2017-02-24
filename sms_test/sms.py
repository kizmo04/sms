import json
import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_PATH = os.path.join(ROOT_PATH, '.conf')
config = json.loads(open(os.path.join(CONF_PATH, 'settings_local.json')).read())

