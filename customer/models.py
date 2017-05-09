from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    
    name = models.CharField('Customer',max_length=250, blank=False)
    image = models.ImageField('Image',blank=True, max_length=500)
    is_company = models.BooleanField('Is comapany', blank=True)
    mobile = models.BigIntegerField('Mobile', blank=True)
    email = models.EmailField('Email', blank=True)
    
    def __unicode__(self):
        return self.name
