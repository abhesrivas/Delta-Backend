from django.contrib import admin
from UserAPI.models import *

# Register your models here.
admin.site.register(User)

# Readonly Fields
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('primary_color', 'secondary_color')
