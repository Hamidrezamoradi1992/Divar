from dataclasses import Field

from rest_framework import serializers
from .models import State, Category, FieldCategory, Advertising, City, SaveValueField


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
                  'value')

#end main serializers

# class ViewCategorySerializer(MainCategorySerializer):
#     parent=serializers.SerializerMethodField()
#     class Meta:
#         model = Category
#         fields = ('title',
#                   'parent',
#                   'free',
#                   'fields',
#                   'price')
#
#     def get_parent(self, obj):
#         pass

class AllAdvertisingViewSerializer(MainAdvertisingSerializer):
    category=MainCategorySerializer(read_only=True)
    image=serializers.SerializerMethodField()
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


    def get_image(self, obj):
        pass