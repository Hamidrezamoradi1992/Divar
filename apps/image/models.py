from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from apps.account.models import User
from apps.core.models import TimeCreateMixin, LogicalDeleteMixin
from apps.image.validations import validate_image_size


# Create your models here.


class Image(LogicalDeleteMixin, TimeCreateMixin):
    expires_at = None
    name = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'{content_type}product_images/',
                              validators=[validate_image_size])
    order_id = models.PositiveSmallIntegerField()
    alt = models.TextField(blank=True,
                           null=True)
    is_cover = models.BooleanField(default=False)

    generics = GenericForeignKey('content_type',
                                 'order_id')

    def clean(self):
        if not (self.content_type.model in ('category', 'advertising', 'user')):
            raise ValidationError('clas not valid')
        if self.is_cover:
            if self.content_type == 'advertising':
                cover_images = Image.objects.filter(content_type=self.content_type,
                                                    order_id=self.order_id)
                if cover_images.is_:
                    raise ValidationError('Each advertising can only have one cover image.')
        if self.content_type.model in ('category', 'user'):
            validate_image_on_ripit = Image.objects.filter(content_type=self.content_type,
                                                           order_id=self.order_id).exists()
            if validate_image_on_ripit:
                raise ValidationError('Each no user can only have one cover image. .')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}-{self.content_type.model} - {self.alt}"


class KycImage(LogicalDeleteMixin, TimeCreateMixin):
    expires_at = None
    full_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             related_name='kyc_user',
                             related_query_name='kyc_user',
                             null=True, blank=True)
    image_idcard = models.ImageField(upload_to=f'kyc/{full_name}_kyc_images/',
                                     verbose_name='ID Card',
                                     validators=[validate_image_size])
    image_Official_photo = models.ImageField(upload_to=f'kyc/{full_name}_kyc_images/',
                                             verbose_name='Official photo',
                                             validators=[validate_image_size])
    image_letter_of_commitment = models.ImageField(upload_to=f'kyc/{full_name}_kyc_images/',
                                                   verbose_name=' letter of commitment',
                                                   validators=[validate_image_size])

    def clean(self):
        user=KycImage.objects.all().values_list('user', flat=True)
        if self.user in user:
            raise ValidationError('User already exists.')

    def __str__(self):
        return f"{self.user.email}/ kyc images"