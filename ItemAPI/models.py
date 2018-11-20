from django.db import models
from django.utils import timezone
from datetime import date
from django.db import models
from django import forms

#Item Category Names
LAPTOP = "Laptops"
DESKTOP = "Desktops"
WORKSTATION = "Workstations"
SERVER = "Servers"
PROCESSOR = "Processors"
GPU = "GPU"
ACCESSORIES = "Accessories"

#Item Choices
ITEMS_TYPES = ((LAPTOP, "Laptops"), (DESKTOP, "Desktops"), (WORKSTATION, "Workstations"), (SERVER, "Servers"), (PROCESSOR, "Processors"), (GPU, "GPU"), (ACCESSORIES, "Accessories"))

# Item model
class Item(models.Model):
    name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=10, choices=ITEMS_TYPES, null=False)

    def __str__(self):
        return '{} - {}'.format(self.name, self.posted_by)

# Laptop model
class Laptop(models.Model):
    company = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    type_name = models.CharField(max_length=200)
    inches = models.FloatField()
    screen_resolution = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)
    gpu = models.CharField(max_length=200)
    operating_system = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    price_euros = models.FloatField()
    photo_url = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.company, self.product, self.type_name)
