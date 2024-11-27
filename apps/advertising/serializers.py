from dataclasses import Field

from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import State, Category, FieldCategory, Advertising, City, SaveValueField, Image
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


class AddAdvertisingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'alt', 'content_type', 'instance_id', 'file']


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


'''save field'''


class DetailSaveValueFieldSerializer(ViewSaveValueFieldSerializer):
    name_field = serializers.SerializerMethodField(read_only=True)
    field_type= serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SaveValueField
        fields = ('value',
                  'name_field',
                  'field_type')

    def get_field_type(self, obj):
        name_field = FieldCategory.object.get(id=obj.field.id)
        return name_field.type_field


'''save field'''


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

    def get_image(self, obj):
        image = Image.objects.filter(content_type=ContentType.objects.get(model='advertising'), instance_id=obj.id)
        return AddAdvertisingImageSerializer(image, many=True).data


# end view serializers

# add advertise in database
class AddAdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = ('id', 'title', 'description', 'price', 'category', 'state', 'city', 'user')


class AdminAdvertisingViewSerializer(AllAdvertisingViewSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Advertising
        fields = ('id',
                  'title',
                  'description',
                  'image',
                  'category',
                  'is_active',
                  'is_deleted',
                  'diffusion',
                  'expires_at'

                  )

    def get_image(self, obj):
        image = Image.objects.filter(content_type=ContentType.objects.get(model='advertising'),
                                     instance_id=obj.id).first()

        return AddAdvertisingImageSerializer(image).data


class AllAdvertiseViewSerializer(MainAdvertisingSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Advertising
        fields = ('id',
                  'title',
                  'price',
                  'image',
                  )

    def get_image(self, obj):
        image = Image.objects.filter(content_type=ContentType.objects.get(model='advertising'),
                                     instance_id=obj.id).order_by('created_at').first()
        return AddAdvertisingImageSerializer(image).data


"""retrieve advertising"""


class RetrieveCategorySerializer(MainCategorySerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'title',
                  'parent',)


class AllRetrieveAdvertisingViewSerializer(AllAdvertisingViewSerializer):
    category = RetrieveCategorySerializer(read_only=True)
    image = serializers.SerializerMethodField()
    vlue_field = serializers.SerializerMethodField()

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

    def get_image(self, obj):
        image = Image.objects.filter(content_type=ContentType.objects.get(model='advertising'), instance_id=obj.id)
        return AddAdvertisingImageSerializer(image, many=True).data

    def get_vlue_field(self, obj):
        field = SaveValueField.objects.filter(advertising=obj.id)
        return DetailSaveValueFieldSerializer(field, many=True).data

"""retrieve advertising"""
