
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import EmailValidator
from django.db import models
# from apps.core.validators import CustomValidators
# from rest_framework.exceptions import ValidationError
# from django.contrib.auth.base_user import BaseUserManager

# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, **extra_fields):

        password = extra_fields.pop("password")
        user = self.model(**extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(**extra_fields)

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(**extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=False, validators=[EmailValidator])
    password = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(null=True, blank=True,
                              choices=(('FEMALE', 'female'), ('MALE', 'male'), ('OTHER', 'other')), max_length=6)
    is_kyc = models.BooleanField(default=False)
    is_web_manager=models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


# class UserCustomManager(BaseUserManager):
#     def _create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         if password is not None:
#             _ = CustomValidators.password_validator(password=password)
#             if not _:
#                 raise ValidationError('Password must be at least 8 characters')
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
#         return self.create_user(email, password, **extra_fields)

