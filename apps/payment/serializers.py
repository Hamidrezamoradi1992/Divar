from rest_framework import serializers
from .models import Order
from ..advertising.models import Advertising


class AddLadderToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['advertiser']

    def validate(self, attrs):
        user=self.context['request'].user
        advertiser = attrs.get('advertiser')
        order = Order.objects.filter(advertiser=advertiser,user=user)
        if order.exists():
            raise serializers.ValidationError("Order already exists")
        return attrs

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['price'] = 20
        validated_data['title'] = 'ladder'
        validated_data['is_paid'] = True
        return self.Meta.model.objects.get_or_create(**validated_data)
