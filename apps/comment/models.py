from django.db import models
from apps.core.models import TimeCreateMixin, LogicalDeleteMixin
from config import settings
from apps.advertising.models import Advertising


# Create your models here.

class comment(TimeCreateMixin, LogicalDeleteMixin):
    massage = models.TextField(max_length=400, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    advertised = models.ForeignKey(Advertising, on_delete=models.CASCADE)
    expires_at = None

    def __str__(self):
        return f'{self.user} to {self.to_user}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        indexes = [models.Index(fields=['advertised', 'user', 'to_user'])]
