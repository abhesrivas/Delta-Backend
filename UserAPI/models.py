from django.db import models
from django.db.models import CharField, IntegerField
from django.dispatch import receiver
from django.db.models.signals import post_save
from . import dominant

# Authentication user model
# User Type Choices
BANK = "Bank"
MEDI = "HealthCare"
SCHOOL = "Education"
RETAIL = "RetailStores"
MISC = "Others"

COMPANY_TYPES = ((BANK, "Bank"), (MEDI, "HealthCare"), (SCHOOL, "Education"), (RETAIL, "RetailStores"), (MISC, "Others"))

class User(models.Model):
    company_id = models.AutoField(primary_key=True, default=1)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True)
    company_type = models.CharField(max_length=100, choices=COMPANY_TYPES, null=False)
    primary_color = models.CharField(max_length=10, default='00cc99')
    secondary_color = models.CharField(max_length=10, default='00cc99')

    def __str__(self):
        return '{}'.format(self.company_name)

# Profile Role Choices
SHOP = "Shopper"
BUY = "Buyer"
COMPANY_ADMIN = "Company_Admin"

PROFILE_ROLES = ((SHOP,"Shopper"),(BUY,"Buyer"),(COMPANY_ADMIN,"Company_Admin"))

class Profile(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100, choices=PROFILE_ROLES, null=False)
    photo_url = models.CharField(max_length=200, default='https://t4.ftcdn.net/jpg/02/15/84/43/240_F_215844325_ttX9YiIIyeaR7Ne6EaLLjMAmy4GvPC69.jpg')

    def __str__(self):
        return '{} - {}'.format(self.name, self.role)

