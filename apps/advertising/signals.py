from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Advertising, SaveValueField
from apps.advertising.utils.validate_ladder_advertising import ValidateLadderAdvertising
from apps.payment.models import Order


@receiver(post_save, sender=Advertising)
def set_instance_ladder(sender, instance, created, **kwargs):
    if not created:
        print('set_instance_ladder', instance.ladder)
        if instance.ladder:
            ValidateLadderAdvertising(instance, category=instance.category)


@receiver(post_save, sender=SaveValueField)
def set_instance_category(sender, instance, created, **kwargs):
    if created:

        if not instance.category.free:
            order, _ = Order.objects.get_or_create(user=instance.advertising.user,
                                                   title='CATEGORY',
                                                   advertiser=instance.advertising,
                                                   price=instance.category.price,
                                                   is_paid=True
                                                   )
