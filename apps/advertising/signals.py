from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Advertising
from apps.advertising.utils.validate_ladder_advertising import ValidateLadderAdvertising


@receiver(post_save, sender=Advertising)
def set_instance_ladder(sender, instance, created, **kwargs):
    if not created:
        print('set_instance_ladder',instance.ladder)
        if instance.ladder:
            ValidateLadderAdvertising(instance,category=instance.category)
