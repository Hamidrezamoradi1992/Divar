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
    city = models.ForeignKey('City',
                             on_delete=models.CASCADE,
                             related_name='city_advertising',
                             related_query_name='city_advertising')
    state = models.ForeignKey('State',
                             on_delete=models.CASCADE,
                             related_name='city_advertising',
                             related_query_name='city_advertising')
    objects = AdvertisingManager()

    def __str__(self):
        return f'title: {self.title}/category: {self.category}'

    def clean(self):
        category = Category.objects.get(id=self.category.pk)
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
                               related_query_name='children',
                               on_delete=models.SET_NULL)
    free = models.BooleanField(default=True)
    fields = models.ManyToManyField(
        'FieldCategory',
        related_name='categories',
        related_query_name='categories',
        blank=True
    )
    price = models.FloatField(default=0)

    def __str__(self):
        return f'title: {self.title}/free: {self.free}'

    def clean(self):
        if not self.parent and self.pk and self.fields.exists():
            has_children = Category.objects.filter(parent_id=self.id).exists()
            print('has_children')
            if has_children and self.fields.exists():
                raise ValidationError('Category with children cannot have fields.')
        if self.free and self.price > 0:
            raise ValidationError('Price cannot be greater than 0 for free categories.')
        elif not self.free and self.price <= 0:
            raise ValidationError('Price must be greater than 0 for non-free categories.')

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if it's a new object
            print('if not self.id')
            super().save(*args, **kwargs)  # Save to get an ID
        self.clean()  # Call clean after saving for validations involving many-to-many
        super().save(*args, **kwargs)

    @staticmethod
    def calculate_max_depth(root_category):

        """
        Recursively calculates the maximum depth of the category tree starting from a given root category.
        """

        if not root_category.children.exists():
            return 0
        else:
            return 1 + max(Category.calculate_max_depth(sub) for sub in root_category.children.all())

    def get_descendants(self, include_self=False, levels=None):

        """
        Fetch all descendants of the current category using dynamically determined levels of prefetching.
        If 'levels' is not provided, calculate it based on the maximum depth of the category tree.
        """

        if levels is None:
            levels = Category.calculate_max_depth(self)

        result = [self] if include_self else []
        queryset = Category.objects.all()

        for _ in range(levels):
            queryset = queryset.prefetch_related('subcategories')

        categories = queryset.filter(id=self.id)

        # noinspection PyShadowingNames
        def collect_categories(category, current_level):

            if current_level > 0:
                for subcategory in category.subcategories.all():
                    result.append(subcategory)
                    collect_categories(subcategory, current_level - 1)

        for category in categories:
            collect_categories(category, levels)

        return result

    def get_parents(self, includes_self=False, levels=None) -> list:
        '''if level back parent category '''
        level = Category.objects.count() if levels is None else levels
        category_list = [self] if includes_self else []
        parent = self.parent
        for _ in range(level):
            if parent is not None:
                category_list.append(c := parent)
                parent = c.parent
            else:
                break
        category_list.reverse()
        return category_list

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        indexes = [models.Index(fields=['title'])]


class FieldCategory(LogicalDeleteMixin, TimeCreateMixin):
    expires_at = None
    title = models.CharField(max_length=120, unique=True)
    type_field = models.CharField(max_length=6,
                                  choices=(('int', 'Int'),
                                           ('str', 'STRING'),
                                           ('float', 'FLOAT'),
                                           ('bool', 'BOOL'),))
    mandatory = models.BooleanField(default=False)
    object = BasicLogicalDeleteManager()

    def clean(self):
        if self.title in ['price', 'title', 'description']:
            raise ValidationError('title already exists')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'title: {self.title} /type: {self.type_field} /mandatory: {self.Mandatory}'


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


class SaveValueField(LogicalDeleteMixin, TimeCreateMixin):
    expires_at = None
    advertising = models.ForeignKey(Advertising, on_delete=models.CASCADE,
                                    related_name='values_advertise',
                                    related_query_name='value_advertise')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='values_category',
                                 related_query_name='values_category')
    field = models.ForeignKey(FieldCategory, on_delete=models.CASCADE,
                              related_name='values_field',
                              related_query_name='values_field')
    value = models.CharField(max_length=255)

    object = BasicLogicalDeleteManager()

    def clean(self):
        if self.field in self.category.fields.all():
            filed_type = self.field.type_field
            self.value = self.value.strip()
        else:
            raise ValidationError('Field no match of category')

        validation_methods = {
            'int': self._validate_int,
            'str': self._validate_str,
            'float': self._validate_float,
            'bool': self._validate_bool
        }

        if filed_type in validation_methods:
            validation_methods[filed_type]()
        else:
            raise ValidationError(f'Unsupported field type: {filed_type}')

    def _validate_int(self):
        if not self.value.isdigit():
            raise ValidationError('Value must be an integer without any letters or special characters.')

    def _validate_str(self):
        if self.value.isdigit():
            raise ValidationError('Value must be a string and not consist solely of digits.')

    def _validate_float(self):
        if not self.value.replace('.', '', 1).isdigit():
            raise ValidationError('Value must be a valid float number.')
        self.value = float(self.value)

    def _validate_bool(self):
        if self.value.lower() not in ['1', '0']:
            raise ValidationError("Value must be a boolean represented as  '1', or '0'.")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
