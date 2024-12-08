from rest_framework import serializers
from .models import Order, OrderItem


class AddLadderToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['advertise']

    def create(self, validated_data):
        print(self)
        order_id, _ = Order.objects.get_or_create(user=self.context['request'].user)
        print(order_id)
        validated_data['order'] = order_id
        validated_data['price_at_order'] = 20
        validated_data['title'] = 'ladder'
        return self.Meta.model.objects.get_or_create(**validated_data)
