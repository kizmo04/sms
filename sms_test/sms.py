import json
import os
import sys

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_PATH = os.path.join(ROOT_PATH, '.conf')
config = json.loads(open(os.path.join(CONF_PATH, 'settings_local.json')).read())

api_key = config['sms']['api_key']
api_secret = config['sms']['api_secret']

params = dict()
params['type'] = 'sms'
params['to'] = '01088605889'
params['from'] = config['sms']['sender_number']
params['text'] = '테스트입니다'
cool = Message(api_key, api_secret)

try:
    response = cool.send(params)
    print("Success Count : %s" % response['success_count'])
    print("Error Count : %s" % response['error_count'])
    print("Group ID : %s" % response['group_id'])

    if "error_list" in response:
        print("Error List : %s" % response['error_list'])

except CoolsmsException as e:
    print("Error Code : %s" % e.code)
    print("Error Message : %s" % e.msg)

sys.exit()
