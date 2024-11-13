from django.contrib import admin

from apps.advertising.models import Category
from apps.image.models import Image, KycImage

# Register your models here
admin.site.register(Image)
admin.site.register(KycImage)
