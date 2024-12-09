from django.db import models
from apps.core.models.logicaldelete import LogicalDeleteMixin
from apps.core.models.timelogical import TimeCreateMixin
from apps.core.managers import BasicLogicalDeleteManager
from django.contrib.auth import get_user_model
from apps.advertising.models import Advertising

User = get_user_model()


class OrderManager(BasicLogicalDeleteManager):
    def completed(self):
        return self.get_queryset().filter(is_completed=True)

    def not_completed(self):
        return self.get_queryset().filter(is_completed=False)

    def paid(self):
        return self.get_queryset().filter(is_paid=True)

    def not_paid(self):
        return self.get_queryset().filter(is_paid=False)


class Order(LogicalDeleteMixin, TimeCreateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    is_completed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    expires_at = None
    objects = OrderManager()

    def __str__(self):
        return str(self.id)

    @property
    def total_order_price(self):
        return sum(item.price_at_order for item in self.items.all())

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['is_completed']),
            models.Index(fields=['is_paid']),
        ]


class OrderItem(LogicalDeleteMixin):
    advertise = models.ForeignKey(Advertising, on_delete=models.CASCADE, related_name='advertise_order_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', related_query_name='items')
    price_at_order = models.FloatField()
    title = models.CharField(null=True,
                             blank=True,
                             choices=(('CATEGORY', 'category'),
                                      ('LADDER', 'ladder')),
                             max_length=10)
    objects = BasicLogicalDeleteManager()



    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('advertise', 'order')
