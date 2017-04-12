import json
import os
import sys

from pathlib import Path
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_PATH = os.path.join(ROOT_PATH, '.conf')
config = json.loads(open(os.path.join(CONF_PATH, 'settings_local.json')).read())

api_key = config['sms']['api_key']
api_secret = config['sms']['api_secret']

params = dict()
params['type'] = 'mms'
params['to'] = '01067675319'
params['from'] = config['sms']['sender_number']
params['text'] = 'hello'
params['image'] = '/Users/kizmo04/Desktop/fsociety.png'
# params['image'] = 'https://igcdn-photos-c-a.akamaihd.net/hphotos-ak-xpt1/t51.2885-15/11142158_1389784811347226_911801625_n.jpg'
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
