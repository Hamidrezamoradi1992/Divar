from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Order,OrderItem
from apps.advertising.utils.validate_ladder_advertising import ValidateLadderAdvertising
from apps.payment.models import Order, OrderItem
from time import sleep

@receiver(post_save, sender=Order)
def set_instance_ladder(sender, instance, created, **kwargs):
    if not created:
        print('hamid')
        if instance.is_paid and instance.is_completed:
            orderItems = OrderItem.objects.filter(order=instance)
            for order_item in orderItems:
                advertiser = order_item.advertise
                if order_item.title == 'ladder':
                    advertiser.ladder = True
                else:
                    advertiser.payed = True
                advertiser.save()



