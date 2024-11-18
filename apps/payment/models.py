from django.db import models
from apps.core.models.logicaldelete import LogicalDeleteMixin
from apps.core.models.timelogical import TimeCreateMixin
from apps.core.managers import BasicLogicalDeleteManager
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Order(LogicalDeleteMixin, TimeCreateMixin):
    expires_at = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order', related_query_name='user_order')
    title = models.CharField(null=True,
                             blank=True,
                             choices=(('CATEGORY', 'category'),
                                      ('LADDER', 'ladder')),
                             max_length=10)
    price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.title}-{self.price}'

    def clean(self):
        if self.title=='category':
            self.price=20000.0

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)




class PriceFunctionalServices(LogicalDeleteMixin, TimeCreateMixin):
    expires_at = None
    title = models.CharField(max_length=70)
    price = models.FloatField(default=0)

