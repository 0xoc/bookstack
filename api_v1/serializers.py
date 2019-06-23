from abc import ABC

from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import UserProfile


class UserProfileGetOrCreate(serializers.ModelSerializer):
    """
    intended to be used only for getting phone number from API
    NOT LOGIN IN SERIALIZER
    """

    class Meta:
        model = UserProfile
        fields = ['phone_number']
