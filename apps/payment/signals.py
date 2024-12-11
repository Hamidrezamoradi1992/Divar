from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Order,OrderItem
from apps.advertising.utils.validate_ladder_advertising import ValidateLadderAdvertising
from apps.payment.models import Order, OrderItem
from time import sleep

from ..advertising.models import Advertising


@receiver(post_save, sender=Order)
def set_instance_ladder(sender, instance, created, **kwargs):
    if not created:
        print('hamid')
        if instance.is_paid and instance.is_completed:
            order_items_ladder = OrderItem.objects.filter(order=instance, title='ladder')
            advertise_ids = order_items_ladder.values_list('advertise_id', flat=True)
            Advertising.objects.filter(id__in=advertise_ids).update(ladder=True)
            orderItems_category = OrderItem.objects.filter(order=instance, title='CATEGORY')
            advertise_ids = orderItems_category.values_list('advertise_id', flat=True)
            Advertising.objects.filter(id__in=advertise_ids).update(payed=True)


