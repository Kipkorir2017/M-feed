from .models import User,Profile,Survey,Reports
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"