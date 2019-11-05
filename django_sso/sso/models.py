from django.db import models

# Create your models here.
from django.utils.translation import string_concat


class SsoConfig(models.Model):

    name = models.CharField(blank=False,null=False,max_length=250)
    metadata_file = models.FileField(upload_to='uploads/meta',null=True,blank=True)
    metadata_url = models.CharField(max_length=1000,blank=True)
    entity_id = models.CharField(null=False,max_length=1000,blank=True)
    acs = models.CharField(max_length=1000,blank=True)

