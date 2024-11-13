from django.contrib import admin
from apps.advertising.models import Category, FieldCategory

# Register your models here.
admin.site.register(Category)
admin.site.register(FieldCategory)
