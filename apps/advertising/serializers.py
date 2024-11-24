from dataclasses import Field

from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import State, Category, FieldCategory, Advertising, City, SaveValueField,Image
from apps.account.models import User
from apps.account.serializers import MainUserSerializer



class MainStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id',
                  'title',
                  'area_code')


class MainFieldCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldCategory
        fields = ('id',
                  'title',
                  'type_field',
                  'mandatory')


class MainAdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = ('id',
                  'title',
                  'description',
                  'price',
                  'category',
                  'state',
                  'city',
                  'diffusion')


class MainCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'state', 'title')


class MainCategorySerializer(serializers.ModelSerializer):
    fields = MainFieldCategorySerializer(many=True)
    parent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id',
                  'title',
                  'parent',
                  'free',
                  'fields',
                  'price',
                  'image')

    def get_parent(self, obj):
        return MainCategorySerializer(obj.parent).data


class MainSaveValueFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveValueField
        fields = ('id',
                  'advertising',
                  'category',
                  'field',
                  'value',)


# end main serializers

# view serializers
class ViewFieldCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldCategory
        fields = ('id',
                  'title',
                  'type_field',
                  'mandatory')


class ViewCategorySerializer(MainCategorySerializer):
    parent = serializers.SerializerMethodField(read_only=True)
    fields = ViewFieldCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('title',
                  'parent',
                  'free',
                  'fields',
                  'price',
                  'image')

    def get_parent(self, obj):
        pass


class ViewSaveValueFieldSerializer(MainSaveValueFieldSerializer):
    name_field = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SaveValueField
        fields = ('id',
                  'advertising',
                  'category',
                  'field',
                  'value',
                  'name_field')

    def get_name_field(self, obj):
        name_field = FieldCategory.object.get(id=obj.field.id)
        return name_field.title


class AddressViewSerializer(MainUserSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'phone',
                  'is_kyc',
                  'address',
                  )


class AllAdvertisingViewSerializer(MainAdvertisingSerializer):
    category = MainCategorySerializer(read_only=True)
    state = MainStateSerializer(read_only=True)
    city = MainCitySerializer(read_only=True)
    image = serializers.SerializerMethodField()
    vlue_field = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = Advertising
        fields = ('id',
                  'title',
                  'description',
                  'price',
                  'image',
                  'category',
                  'state',
                  'city',
                  'vlue_field',
                  'address',)


    def get_vlue_field(self, obj):
        field = SaveValueField.objects.filter(advertising=obj.id)
        return ViewSaveValueFieldSerializer(field, many=True).data

    def get_address(self, obj):
        if self.context['request'].user.is_authenticated:
            user = User.objects.filter(pk=self.context['request'].user.id)
            return AddressViewSerializer(user, many=True).data
        return {'massage': 'is_user_not_authentication'}
# end view serializers

# add advertise in database
class AddAdvertisingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Advertising
            fields = ['id', 'title', 'description', 'price', 'category', 'state', 'city', 'user']
