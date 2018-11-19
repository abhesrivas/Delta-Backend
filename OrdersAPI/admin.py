from django.contrib import admin
from OrdersAPI.models import *

# Register your models here.
admin.site.register(Order)
admin.site.register(Quote)

# Readonly Fields
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'requoted_at')

class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at')