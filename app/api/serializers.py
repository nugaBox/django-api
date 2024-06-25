from .models import *
from rest_framework import serializers, viewsets


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class ApiHistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiHist
        fields = '__all__'