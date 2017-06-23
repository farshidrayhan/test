from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import models



class indexForm(forms.Form):
    # post = forms.CharField()


    name = forms.CharField(max_length=50,label='Name')
    mail = forms.CharField(max_length=50,label='Mail' )

