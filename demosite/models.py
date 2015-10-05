import datetime

from django.db import models
from django.utils import timezone


class Quotes(models.Model):
    quotes = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    name =models.CharField(max_length=200)
    def __str__(self):             
        return self.name
    
