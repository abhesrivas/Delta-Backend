from OrdersAPI.models import *
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('__all__')