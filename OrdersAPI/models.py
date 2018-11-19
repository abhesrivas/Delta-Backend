from django.db import models
from django.utils import timezone
from datetime import date
from django.db import models
from django import forms
from OrdersAPI.models import *

# Quote Model
class Quote(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(editable=False)
    requoted_at = models.DateTimeField(editable=False)
    created_by = models.CharField(max_length=200)
    authorized_buyer = models.CharField(max_length=200)
    expires = models.DateTimeField(editable=False)
    subtotal = models.FloatField()

    #Overiding Save Function to Automatically input DateTime
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
            self.expires = created_at + timedelta(days=30)
        self.requoted_at = timezone.now()
        return super(Quote, self).save(*args, **kwargs)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.number, self.name, self.authorized_buyer, self.created_by)

class Order(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(editable=False)
    created_by = models.CharField(max_length=200)
    subtotal = models.FloatField()

    #Overiding Save Function to Automatically input DateTime
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return '{} - {} - {}'.format(self.number, self.name, self.created_by)