from rest_framework import serializers
from apps.account.models import User


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
                  'age',
                  'image_idcard',
                  'image_Official_photo',
                  'image_letter_of_commitment')


class UpdateUserSerializer(MainUserSerializer):
    class Meta:
        model = User

        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'phone',
                  'is_kyc',
                  'gender',
                  'address',
                  'age',
                  'image_idcard',
                  'image_Official_photo',
                  'image_letter_of_commitment')
        extra_kwargs = {
            'email': {'read_only': True},
            'is_kyc': {'read_only': True},
        }

    def update(self, instance, validated_data):
        fields_to_update = ('first_name', 'last_name', 'phone', 'gender', 'address', 'age', 'image_idcard',
                            'image_Official_photo', 'image_letter_of_commitment')
        for field in fields_to_update:
            if field in validated_data and validated_data[field] not in [None,""]:
                setattr(instance, field, validated_data[field])
            else:
                instance_none=User.objects.filter(pk=instance.pk).values_list(field, flat=True)
                setattr(instance, field, instance_none.first())

        instance.save()
        return instance
