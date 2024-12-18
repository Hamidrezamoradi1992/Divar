from django.contrib import admin
from django.db.models import Q
from apps.advertising.models import Category, FieldCategory, Advertising, SaveValueField, City,State,Image,CategoryField

# Register your models here.

class FieldCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']  # فرض بر این است که فیلد name وجود دارد

class AdvertisingAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']  # فرض بر این است که title و description وجود دارند

class SaveValueFieldAdmin(admin.ModelAdmin):
    search_fields = ['title']

class CityAdmin(admin.ModelAdmin):
    search_fields = ['title']

class StateAdmin(admin.ModelAdmin):
    search_fields = ['title']
class ImageAdmin(admin.ModelAdmin):
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
admin.site.register(Category, CategoryAdmin)


admin.site.register(FieldCategory, FieldCategoryAdmin)
admin.site.register(Advertising, AdvertisingAdmin)
admin.site.register(SaveValueField, SaveValueFieldAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(CategoryField)






