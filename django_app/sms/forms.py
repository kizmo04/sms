import re

from django import forms
from django.core.exceptions import ValidationError


class MessageForm(forms.Form):
    recipient_numbers = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'size': 100
            }
        ))
    content = forms.CharField(widget=forms.Textarea())

    def clean_recipient_numbers(self):
        cleaned_numbers = []
        error_numbers = []
        p = re.compile(r'^0\d{9}\d?')
        number_string = self.cleaned_data['recipient_numbers']
        # 공백문자 또는 -문자는 빈문자열로 바꿔준다
        numbers_sub = re.sub(r'\s|-', '', number_string)
        # , 또는 .을 기준으로 문자열을 나누어 리스트로 반환해 numbers에 할당
        numbers = re.split(r',|\.', numbers_sub)
        # numbers = number_string.replace('-', '').replace(' ', '').split(',')
        for number in numbers:
            if re.match(p, number):
                cleaned_numbers.append(number)
            else:
                error_numbers.append(number)
        if error_numbers:
            raise ValidationError('Invalid phone number')

        return cleaned_numbers
