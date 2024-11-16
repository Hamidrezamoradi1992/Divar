from django.db import models


class BasicLogicalDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_deleted=False)

    def archive(self):
        return super().get_queryset().all()

