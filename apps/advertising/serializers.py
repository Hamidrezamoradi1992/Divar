from dataclasses import Field

from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import State, Category, FieldCategory, Advertising, City, SaveValueField
# from django.contrib.auth import get_user_model
# User = get_user_model()
from apps.account.models import User
from apps.account.serializers import MainUserSerializer
from apps.core.serializers import MainImageSerializer
from apps.core.models.images import Image


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
    fields=MainFieldCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ('title',
                  'parent',
                  'free',
                  'fields',
                  'price')


class MainSaveValueFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaveValueField
        fields = ('id',
                  'advertising',
                  'category',
                  'field',
                  'value',)




# end main serializers
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
                  'price')

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

class AdresViewSerializer(MainUserSerializer):
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
                  'diffusion',
                  'category',
                  'state',
                  'city',
                  'vlue_field',
                  'address',)


    def get_image(self, obj):
        content_type = ContentType.objects.get(model='advertising')
        image=Image.objects.filter(content_type=content_type,instance_id=obj.id)
        return MainImageSerializer(image, many=True).data

    def get_vlue_field(self, obj):
        field = SaveValueField.objects.filter(advertising=obj.id)
        print(field)
        return ViewSaveValueFieldSerializer(field, many=True).data

    def get_address(self, obj):
        print(self.context['request'].user.is_authenticated)
        if self.context['request'].user.is_authenticated:
            user=User.objects.filter(pk=self.context['request'].user.id)
            return AdresViewSerializer(user, many=True).data
        return {'massage': 'is_user_not_authentication'}

