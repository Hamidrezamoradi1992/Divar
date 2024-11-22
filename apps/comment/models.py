from django.db import models
from apps.core.models.logicaldelete import LogicalDeleteMixin
from apps.core.models.timelogical import TimeCreateMixin

from apps.advertising.models import Advertising
from apps.core.managers import BasicLogicalDeleteManager
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class comment(TimeCreateMixin, LogicalDeleteMixin):
    massage = models.TextField(max_length=400, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_comments',related_query_name='user_comments')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='to_user_comments',related_query_name='to_user_comments')
    advertised = models.ForeignKey(Advertising, on_delete=models.CASCADE)
    expires_at = None

    objects = BasicLogicalDeleteManager()

    def __str__(self):
        return f'{self.user} to {self.to_user}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        indexes = [models.Index(fields=['advertised', 'user', 'to_user'])]
