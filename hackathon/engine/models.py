from django.db import models
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    # print(instance.__class__.__name__)
    if(instance.__class__.__name__=="Found"):
        upload_to = os.path.join('images','Found')
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(instance.name, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)
    else:
        upload_to = os.path.join('images','Lost')
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(instance.name, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)
# Create your models here.
class Lost(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField( max_length=255)
    itemname = models.CharField( max_length=255)
    email = models.CharField( max_length=255)
    
    
    image = models.ImageField(upload_to=path_and_rename, default="")
    def __str__(self):
        return self.itemname

class Found(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField( max_length=255)
    itemname = models.CharField( max_length=255)
    email = models.CharField( max_length=255)
    
    
    image = models.ImageField(upload_to=path_and_rename, default="")


    def __str__(self):
        return self.itemname

