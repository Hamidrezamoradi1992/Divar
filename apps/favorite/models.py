from django.db import models
from apps.core.models.logicaldelete import LogicalDeleteMixin
from django.contrib.auth import get_user_model
from apps.core.managers import BasicLogicalDeleteManager
from apps.advertising.models import Advertising
User = get_user_model()

# Create your models here.


class Favorite(LogicalDeleteMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_query_name="user_favorites", related_name='user_favorites')
    products = models.ForeignKey(Advertising, on_delete=models.CASCADE, related_query_name="advertising_favorites",
                                 related_name='advertising_favorites')

    objects = BasicLogicalDeleteManager()

    def __str__(self):
        return f"{self.user} -> {self.products}"