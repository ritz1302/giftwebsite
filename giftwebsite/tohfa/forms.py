import datetime
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from simplemathcaptcha.fields import MathCaptchaField




class CreateAcount(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model= User
        fields= ('username', 'first_name', 'last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(CreateAcount, self).__init__(*args, **kwargs)
