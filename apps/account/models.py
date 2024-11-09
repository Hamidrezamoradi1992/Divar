from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from apps.core.validators import CustomValidators
from rest_framework.exceptions import ValidationError


# Create your models here.

class UserCustomManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        _ = CustomValidators.password_validator(password=password)
        if not _:
            raise ValidationError('Password must be at least 8 characters')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=False, validators=[EmailValidator])
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(null=True, blank=True,
                              choices=(('FEMALE', 'female'), ('MALE', 'male'), ('OTHER', 'other')), max_length=6)
    is_kyc = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserCustomManager()
