from django.db import models


# Create your models here.
class LogicalDelete(models.Model):
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
