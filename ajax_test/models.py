from django.db import models

# Create your models here.

class Drugs(models.Model):    #
    drug  = models.CharField(max_length=50)
    fingerprint  = models.CharField(max_length=900)
    name  = models.CharField(max_length=150)


    def __str__(self):
        return self.name