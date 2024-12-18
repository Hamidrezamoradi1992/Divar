from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save,m2m_changed

from apps.advertising.models import Advertising, SaveValueField,Category
from apps.advertising.utils.validate_ladder_advertising import ValidateLadderAdvertising
from apps.payment.models import Order, OrderItem
from django.core.exceptions import ValidationError


@receiver(post_save, sender=SaveValueField)
def set_instance_category(sender, instance, created, **kwargs):
    if created:
        if not instance.category.free:
            order, _ = Order.objects.get_or_create(user=instance.advertising.user,is_completed=False)
            order_item, _ = OrderItem.objects.get_or_create(order=order,
                                                            title='CATEGORY',
                                                            advertise=instance.advertising,
                                                            price_at_order=instance.category.price)




def validate_fields_with_children(sender, instance, action, **kwargs):
    if action == "post_add":
        if instance.children.exists():
            pass


m2m_changed.connect(validate_fields_with_children, sender=Category.fields.through)