from django.core.files.storage import FileSystemStorage,Storage
from django.db import Error
from django.db.backends import sqlite3
from sqlite3 import connect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.conf import settings
import os
from sklearn.externals import joblib
import csv
import numpy as np
from . import pssm_to_bigram,spider_to_structural_info,\
    spider_to_auto_covar_generate,spider_to_bigram,drug_list_generator
from django.views import generic
from django.views.generic import FormView
from music.forms import indexForm2 as indexForm
# from ajax_test.form import indexForm
from .models import Drugs
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
        """Returns a filename that's free on the target storage system, and
        available for new content to be written to.

        Found at http://djangosnippets.org/snippets/976/

        This file storage solves overwrite on upload problem. Another
        proposed solution was to override the save method on the model
        like so (from https://code.djangoproject.com/ticket/11663):

        def save(self, *args, **kwargs):
            try:
                this = MyModelName.objects.get(id=self.id)
                if this.MyImageFieldName != self.MyImageFieldName:
                    this.MyImageFieldName.delete()
            except: pass
            super(MyModelName, self).save(*args, **kwargs)
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name



class IndexView(generic.ListView):

    template_name = 'ajax_test/index.html'
    # context_object_name = 'all_albums' # now the returned list is stored in this var for the html to know

    # def get_queryset(self):
    #     return Album.objects.all()

    def get(self, request):
        form = indexForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = indexForm(request.POST,request.FILES)

        print(form)
        # spd = request.FILES['spd']
        error = ''

        # database connection
        try:
            conn = connect('db.sqlite3')
            print("connected")
            # return conn
        except Error as e:
            print(e)



        # getting data from form
        # spd = 'faka !!!'
        if form.is_valid():
            print("valid")
            target_group = form.cleaned_data['target_group']
            print('done !!!')
            spd = form.cleaned_data['spd']
            print('done !!!')
            pssm = form.cleaned_data['pssm']
            print('done !!!')
            drug = form.cleaned_data['drug']
            print('done !!!')
        else:
            print("form not valid !!!!")
        # print("type ", type(spd))
        # trying to load txts rcved
        try:

            spd_file = spd.readline()
            pssm_file = pssm.readline()

            # print(Drugs.objects.get(drug=drug).fingerprint)
            drug_file = Drugs.objects.get(name=drug).fingerprint
            # prints the lines in the console
            # print("spd file " , spd_file)
            # print("pssm file " , pssm_file)
            # print("drug file " , drug_file)



        except TypeError:
            error = 'not valid text file'

        # for storing the temporary file
        fs = FileSystemStorage()
        #
        # ## removing the previous files
        chk = OverwriteStorage().get_available_name('spd')
        chk = OverwriteStorage().get_available_name('pssm')
        # chk = OverwriteStorage().get_available_name('drug')
        #
        media_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'media')
        #
        media_path.strip(' ')
        file_spd = fs.save('spd', spd )
        file_pssm = fs.save('pssm', pssm )
        # file_drug = fs.save('drug', drug )
        #
        spd_file_url = fs.url(file_spd)
        spd = media_path + '/spd'
        pssm = media_path + '/pssm'
        enzyme_path = media_path + '/'+ target_group + '.pkl'

        print(target_group)

        clf_e = joblib.load(enzyme_path)

        zero_class = 0
        one_class = 0

        try:

            structural_info =  spider_to_structural_info.spider_to_structural_info(spd)
            auto_co_var = spider_to_auto_covar_generate.spider_to_auto_covar(spd)
            bigram_spider = spider_to_bigram.spider_to_spider(spd)
            bigram_pssm = pssm_to_bigram.pssm_to_bigram(pssm)

            feature_list = []

            drug_file = drug_file.split()
            drug_file = list(map(int,drug_file))
            # drug_file = drug_file.strip('')
            # drug_file.remove('')
            drug_file = drug_list_generator.list_filler(drug_file)

            # for v in drug_file:
            #     if v == '':
            #
            # print(drug_file)
            # print(type(drug_file.split(',')))
            # print(type(drug_file))
            # drug_file.split(',')
            # feature_list = sum(feature_list,drug_file)
            # print(len(feature_list))

            # making feature list
            feature_list = drug_file
            feature_list = feature_list + bigram_pssm
            feature_list = feature_list + structural_info
            feature_list = feature_list + auto_co_var
            feature_list = feature_list + bigram_spider
            # print(len(feature_list))

            prediction = clf_e.predict_proba(feature_list)

            zero_class = prediction[0][0]
            one_class = prediction[0][1]
        except  :
            error = "faulty file"
            print(error)



        # pssm_file_url = fs.url(file_pssm)
        # drug_file_url = fs.url(file_drug)

        # all data to be sent as a result of the request
        dict = {
            'dataset': target_group,
            'form' : 'null',
            # 'file_spd':spd_file,
            # 'file_pssm':pssm_file,
            'zero_class':zero_class,
            'one_class':one_class,
            # 'file_drug':drug_file,
            'error':error


        }
        args = dict # dictonary is sent as an argument
        return render(request, self.template_name, args)

class DownloadsView(generic.TemplateView):
    template_name = 'ajax_test/downloads.html'


class InstructionsView(generic.TemplateView):
    template_name = 'ajax_test/instructions.html'

class ContributorsView(generic.TemplateView):

    template_name = 'ajax_test/contributors.html'

