from rest_framework import serializers
from UserAPI.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('company_id','company_name','location','company_type')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'role', 'photo_url')

