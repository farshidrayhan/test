from django.contrib import admin
from .models import  Album,Song,Drugs

# Register your models here.

admin.site.register(Album) # adds these tables in the admin panel under this apps name
admin.site.register(Song)
admin.site.register(Drugs)

