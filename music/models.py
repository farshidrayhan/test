from django.db import models
from django.core.urlresolvers import reverse

# after changing DB do this 2 commands

# 1. python manage.py makemigrations music
# 2. python manage.py migrate





# Create your models/db_tables here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_name = models.CharField(max_length=100)
    genre = models.CharField(max_length= 150)
    album_logo = models.FileField()

    def __str__(self):   # these are given so that a str representation is shown of the object
        return self.artist + " " + self.album_name

    def get_absolute_url(self): # returns the view with the primary key
        return reverse('music:detail',kwargs={'pk':self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title  = models.CharField(max_length=250)
    file_type = models.CharField(max_length= 10)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.song_title
    #
    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.album_id})


class Drugs(models.Model):    #
    drug  = models.CharField(max_length=50)
    fingerprint  = models.CharField(max_length=900)
    name  = models.CharField(max_length=150)


    def __str__(self):
        return self.name