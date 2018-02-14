

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import models
from .models import Drugs

class indexForm(forms.Form):
    # post = forms.CharField()
    enzyme = 'enzyme'
    nr = 'nr'
    gpcr = 'gpcr'
    ic = 'ic'

    dataset_choice = (
        (ic, 'IC'),
        (enzyme, 'Enzyme'),
        (nr, 'Nuclear Receptor'),
        (gpcr, 'GPCR'),
    )
    target_group = forms.ChoiceField(choices=dataset_choice)
    spd = forms.FileField()
    pssm = forms.FileField()
    drug = forms.ModelChoiceField(queryset=Drugs.objects.all().order_by('drug'))
