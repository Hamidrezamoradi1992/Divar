from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models
from apps.core.models.logicaldelete import LogicalDeleteMixin
from apps.core.models.timelogical import TimeCreateMixin
from apps.core.validators import CustomValidators
from apps.core.managers import BasicLogicalDeleteManager


# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
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
        extra_fields.setdefault("sait_admin", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(**extra_fields)


class User(AbstractUser):
    username = None
    password = models.CharField(max_length=128, blank=True, null=True, unique=False)
    email = models.EmailField(unique=True, null=False,
                              validators=[EmailValidator])
    phone = models.CharField(max_length=11,
                             null=True,
                             blank=True)
    address = models.CharField(max_length=250,
                               null=True,
                               blank=True)
    age = models.IntegerField(null=True,
                              blank=True)
    gender = models.CharField(null=True,
                              blank=True,
                              choices=(('FEMALE', 'female'),
                                       ('MALE', 'male'),
                                       ('OTHER', 'other')),
                              max_length=6)
    is_kyc = models.BooleanField(default=False)
    sait_admin = models.BooleanField(default=False)
    is_web_manager = models.BooleanField(default=False)

    image_idcard = models.ImageField(upload_to=f'kyc/_kyc_images/',
                                     verbose_name='ID Card',
                                     validators=[CustomValidators.file_validator],
                                     null=True, blank=True,default=None)
    image_Official_photo = models.ImageField(upload_to=f'kyc/_kyc_images/',
                                             verbose_name='Official photo',
                                             validators=[CustomValidators.file_validator],
                                             null=True, blank=True,default=None)
    image_letter_of_commitment = models.ImageField(upload_to=f'kyc/_kyc_images/',
                                                   verbose_name=' letter of commitment',
                                                   validators=[CustomValidators.file_validator],
                                                   null=True, blank=True,default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def clean(self):
        if self.age:
            if self.age > 90 or self.age<18:
                raise ValidationError('Age must be between 18 and 90.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.email}-{self.get_full_name()}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        indexes = [models.Index(fields=['email', 'first_name'])]
