import re
import os
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class CustomValidators:
    _PASSWORD_PATTERN = re.compile(r'^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{6,})\S$')


    @staticmethod
    def file_validator(file):
        if file.name.endswith (('jpg', 'svg', 'png','jpeg','webp')):
            if file.size > 2 * 1024 * 1024:
                raise ValidationError('File size is too big')
        elif file.name.endswith(('.mkv', '.mp4', '.avi', '.wmv','.webp')):
            if file.size > 300 * 1024 * 1024:
                raise ValidationError('File size is too big')
        else:
            raise ValidationError('File type is not allowed')

    @classmethod
    def password_validator(cls, password):
        return re.match(cls._PASSWORD_PATTERN, password)
