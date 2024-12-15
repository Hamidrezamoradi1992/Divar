from rest_framework import serializers
from .models import Order, OrderItem
from rest_framework.exceptions import ValidationError

class AddLadderToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['advertise']

    def create(self, validated_data):
        order_id, _ = Order.objects.get_or_create(user=self.context['request'].user,is_completed=False,is_paid=False)
        if not _:
            _=OrderItem.objects.filter(advertise_id=int(self.data['advertise']),order_id=order_id.id).exists()
            if _:
                raise serializers.ValidationError('comment not found')
        validated_data['order'] = order_id
        validated_data['price_at_order'] = 20
        validated_data['title'] = 'ladder'
        return self.Meta.model.objects.get_or_create(**validated_data)
