from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from apps.core.models.logicaldelete import LogicalDeleteMixin
from apps.core.models.timelogical import TimeCreateMixin
from apps.core.managers import BasicLogicalDeleteManager


# Create your models here.

class AdvertisingManager(BasicLogicalDeleteManager):
    def is_diffusion(self):
        super().get_queryset().filter(diffusion=True)

    def is_ladder(self):
        super().get_queryset().filter(ladder=True)


class CategoryManager(BasicLogicalDeleteManager):
    pass


class Advertising(LogicalDeleteMixin, TimeCreateMixin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0)
    diffusion = models.BooleanField(default=False)
    ladder = models.BooleanField(default=False)
    category = models.ForeignKey('Category',
                                 related_name='advertising',
                                 related_query_name='advertising',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='user',
                             related_query_name='user')
    objects = AdvertisingManager()

    def clean(self):
        category = Category.objects.get(pk=self.category.pk)
        if category.parent:
            raise ValidationError('Categories can not be a parent')
        if not Category.fields:
            raise ValidationError('Categories cannot be empty fields')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Advertising'
        verbose_name_plural = 'Advertising'
        ordering = ['-created_at']
        indexes = [models.Index(fields=['title'])]


class Category(LogicalDeleteMixin, TimeCreateMixin):
    expires_at = None
    title = models.CharField(max_length=120)
    parent = models.ForeignKey('self',
                               null=True,
                               blank=True,
                               related_name='children',
                               on_delete=models.SET_NULL)
    free = models.BooleanField(default=True)
    fields = models.ForeignKey('FieldCategory',
                               on_delete=models.SET_NULL,
                               related_name='fields',
                               related_query_name='fields',
                               null=True,
                               blank=True)

    object = CategoryManager()

    def clean(self):
        if self.fields:
            if self.parent:
                raise ValidationError('no category is parend and fields')
            father = Category.objects.filter(parent_id=self.id).exists()
            if father:
                raise ValidationError('no category is parend and fields')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        indexes = [models.Index(fields=['title'])]


class FieldCategory(LogicalDeleteMixin, TimeCreateMixin):
    expires_at = None
    title = models.CharField(max_length=120, unique=True)
    object = BasicLogicalDeleteManager()

    def clean(self):
        if self.title in ['price', 'title', 'description']:
            raise ValidationError('title already exists')

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'FieldCategory'
        verbose_name_plural = 'FieldCategories'
        indexes = [models.Index(fields=['title'])]


class State(LogicalDeleteMixin, TimeCreateMixin):
    title = models.CharField(max_length=120,
                             unique=True)
    area_code = models.CharField(max_length=3,
                                 unique=True,
                                 null=True,
                                 blank=True)
    expires_at = None
    object = BasicLogicalDeleteManager()

    def __str__(self):
        return f'title: {self.title} / area: {self.area_code}'

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
        indexes = [models.Index(fields=['title', 'area_code'])]


class City(LogicalDeleteMixin, TimeCreateMixin):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state', related_query_name='state')
    title = models.CharField(max_length=120, unique=True)
    expires_at = False
    object = BasicLogicalDeleteManager()

    def __str__(self):
        return f'title: {self.title}'

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        indexes = [models.Index(fields=['title'])]
