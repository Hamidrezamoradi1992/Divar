from django.contrib import admin
from apps.advertising.models import Category, FieldCategory,Advertising

# Register your models here.
admin.site.register(Category)
admin.site.register(FieldCategory)
admin.site.register(Advertising)

