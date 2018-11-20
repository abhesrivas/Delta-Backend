from ItemAPI.models import *
from rest_framework import serializers


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ('id','company','product','type_name','inches','screen_resolution','cpu','ram','memory','gpu','operating_system','weight','price_euros','photo_url')
