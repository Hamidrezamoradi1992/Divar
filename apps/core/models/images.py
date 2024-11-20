from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from apps.core.models.logicaldelete import LogicalDeleteMixin
from apps.core.models.timelogical import TimeCreateMixin
from apps.core.validators import CustomValidators


# Create your models here.


class Image(LogicalDeleteMixin, TimeCreateMixin):
    expires_at = None
    name = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'Image_images/',
                              null=True,
                              blank=True)
    instance_id = models.PositiveSmallIntegerField()
    alt = models.TextField(blank=True,
                           null=True)
    is_cover = models.BooleanField(default=False)

    generics = GenericForeignKey('content_type',
                                 'instance_id')

    def clean(self, **kwargs):
        if not (self.content_type.model in ('category', 'advertising', 'user')):
            raise ValidationError('class not valid')
        if self.is_cover:
            if self.content_type == 'advertising':
                cover_images = Image.objects.filter(content_type=self.content_type,
                                                    instance_id=self.instance_id)
                if cover_images.is_:
                    raise ValidationError('Each advertising can only have one cover image.')
        if self.image:
            CustomValidators.image_validator(self.image)
        if self.content_type.model in ('category', 'user'):
            validate_image_on_ripit = Image.objects.filter(content_type=self.content_type,
                                                           instance_id=self.instance_id).exists()
            # if validate_image_on_ripit:
            #     raise ValidationError('Each no user can only have one cover image.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}-{self.content_type.model}-{self.alt}"

    class Meta:
        pass
