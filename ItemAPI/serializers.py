from ItemAPI.models import *
from rest_framework import serializers


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
fields = ('__all__')