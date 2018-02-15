from django.shortcuts import render
from django.core.files.storage import FileSystemStorage, Storage
from django.db import Error
from django.db.backends import sqlite3
from sqlite3 import connect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
from django.conf import settings
import os
from sklearn.externals import joblib
import csv
import numpy as np

from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from ajax_test.form import indexForm


class IndexView(generic.TemplateView):
    template_name = 'ajax_test/index.html'

    def get(self, request):
        form = indexForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = indexForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']

        dict = {
            'error': '',
            'name': name,
            'form': form,
            'mail': mail

        }
        args = dict  # dictonary is sent as an argument
        return render(request, self.template_name, args)


class DownloadsView(generic.TemplateView):
    template_name = 'ajax_test/downloads.html'


class InstructionsView(generic.TemplateView):
    template_name = 'ajax_test/instructions.html'


class validate_name(generic.CreateView):

    def get(self, request):
        name = request.GET.get('name', None)

        mail = request.GET.get('mail', None)


        try:
            score = float(name) + float(mail)

        except:
            score = 404
    # print(float(name))
    # print(float(mail))
    # print(score)
        data = {
            'is_taken': score
        }

        return JsonResponse(data)
