from django.shortcuts import render
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

from sms.forms import MessageForm
from utils.settings import get_config


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():

            numbers = form.cleaned_data['recipient_numbers']
            text = form.cleaned_data['content']

            for number in numbers:
                send_sms(number, text)

    else:
        form = MessageForm()
    context = {
        'form': form
    }
    return render(request, 'common/index.html', context)


def get_params(to_number, text):
    config = get_config()
    params = dict()
    params['type'] = 'sms'
    params['to'] = to_number
    params['from'] = config['sms']['sender_number']
    params['text'] = text
    return params


def send_sms(number, text):
    config = get_config()
    api_key = config['sms']['api_key']
    api_secret = config['sms']['api_secret']
    params = get_params(number, text)

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
