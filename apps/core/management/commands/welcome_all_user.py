from apps.account.models import User
from django.core.management.base import BaseCommand

from service.email import EmailService


class Command(BaseCommand):
    help = 'Welcome all  email users'
    def handle(self, *args, **options):
        mail=User.objects.all().values_list('email',flat=True)
        email = EmailService(subject='welcome',
                             template_name='mail/welcome.html',
                             to_email=list(mail))
        email.send()