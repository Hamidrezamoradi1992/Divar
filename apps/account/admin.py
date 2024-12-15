from django.contrib import admin
from .models import User
# Register your models here.
class user(admin.ModelAdmin):
    search_fields = ['email']
admin.site.register(User,user)