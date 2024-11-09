import re

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
