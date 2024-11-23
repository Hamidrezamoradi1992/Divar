from django.contrib import admin
from apps.advertising.models import Category, FieldCategory, Advertising, SaveValueField, City,State,Image

# Register your models here.
admin.site.register(Category)
admin.site.register(FieldCategory)
admin.site.register(Advertising)
admin.site.register(SaveValueField)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Image)

