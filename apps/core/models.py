from django.db import models


# Create your models here.
class LogicalDelete(models.Model):
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class TimeCreate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        abstract = True