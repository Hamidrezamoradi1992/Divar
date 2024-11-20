import re
import os
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError


class CustomValidators:
    _PASSWORD_PATTERN = re.compile(r'^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{6,})\S$')

    @staticmethod
    def image_validator(image):
        max_size = 2
        if image.size > max_size * 1024 * 1024:
            raise ValidationError('Image size is too big')

    @classmethod
    def password_validator(cls, password):
        return re.match(cls._PASSWORD_PATTERN, password)

    @classmethod
    def dynamic_upload_path(instance, filename):
        # پیدا کردن مدل مرتبط با content_type
        model_name = instance.content_type.model
        # تولید پوشه بر اساس مدل
        base_folder = f"{model_name}_images"
        # استخراج پسوند فایل
        extension = os.path.splitext(filename)[1]
        # نام فایل با استفاده از slugify
        name = slugify(instance.name) if instance.name else "default"
        # تولید مسیر نهایی فایل
        new_filename = f"{name}_{instance.instance_id}{extension}"
        return os.path.join(base_folder, new_filename)
