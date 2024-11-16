from rest_framework import serializers
from django.contrib.auth.models import User


class SigninUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email')