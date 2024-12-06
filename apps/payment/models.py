from django.db import models
from apps.core.models.logicaldelete import LogicalDeleteMixin
from apps.core.models.timelogical import TimeCreateMixin
from apps.core.managers import BasicLogicalDeleteManager
from django.contrib.auth import get_user_model
from apps.advertising.models import Advertising

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
    advertiser = models.ForeignKey(Advertising, on_delete=models.CASCADE, related_name='advertiser', related_query_name='advertiser')
    is_completed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}-{self.price}-{self.user}'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)






