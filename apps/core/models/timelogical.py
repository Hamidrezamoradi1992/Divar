from django.db import models


class TimeCreateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        abstract = True