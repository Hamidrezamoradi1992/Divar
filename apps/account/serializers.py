from rest_framework import serializers

from apps.core.serializers import MainImageSerializer
from apps.core.models.images import Image
from django.contrib.auth import get_user_model

User = get_user_model()


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'is_active',
                  'phone',
                  'is_kyc',
                  'gender',
                  'address',
                  'age')


class UpdateUserSerializer(MainUserSerializer):
    class Meta:
        model = User

        fields = ['id',
                  'email',
                  'first_name',
                  'last_name',
                  'phone',
                  'gender',
                  'address',
                  'age']
        extra_kwargs = {
            'email': {'read_only': True},
        }


class UpdateImageUserSerializer(MainImageSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'content_type', 'image', 'instance_id', 'alt', 'is_cover')

    def update(self, instance, validated_data):
        print(instance)
        instance.save()
        return instance

