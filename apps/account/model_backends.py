from django.contrib.auth.backends import ModelBackend
from apps.account.models import User

class CustomUserBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        email=kwargs.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None