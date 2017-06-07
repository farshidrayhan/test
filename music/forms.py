from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import models
from .models import  Album,Song,Drugs


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
    dataset = forms.ChoiceField(choices=dataset_choice)
    spd = forms.FileField()
    pssm = forms.FileField()
    drug = forms.ModelChoiceField(queryset=Drugs.objects.all().order_by('drug'))

# class registrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#          model = User
#          fields = (
#              'username',
#              'name',
#              'email',
#              'password1',
#              'password2',
#          )
#
#     def save(self,comitt = True ):
#         user = super(registrationForm,self).save(comitt = False)
#
#         user.name = self.cleaned_data['name']
#         user.name = self.cleaned_data['email']
#
#         if comitt:
#             user.save()
#
#         return user
