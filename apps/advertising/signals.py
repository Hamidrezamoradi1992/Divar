from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Advertising, SaveValueField
from apps.advertising.utils.validate_ladder_advertising import ValidateLadderAdvertising
from apps.payment.models import Order, OrderItem


@receiver(post_save, sender=Advertising)
def set_instance_ladder(sender, instance, created, **kwargs):
    if not created:
        print('signal,set_instance_ladder', instance.ladder)
        if instance.ladder and instance.diffusion:
            ValidateLadderAdvertising(instance, category=instance.category)


@receiver(post_save, sender=SaveValueField)
def set_instance_category(sender, instance, created, **kwargs):
    if created:
        if not instance.category.free:
            order, _ = Order.objects.get_or_create(user=instance.advertising.user,is_completed=False)
            order_item, _ = OrderItem.objects.get_or_create(order=order,
                                                            title='CATEGORY',
                                                            advertise=instance.advertising,
                                                            price_at_order=instance.category.price)
