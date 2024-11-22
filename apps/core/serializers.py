from rest_framework import serializers
from apps.core.models.images import Image


class MainImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','name', 'content_type', 'image', 'instance_id', 'alt', 'is_cover')
