from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.account.models import User
from service.email import EmailService

from django.contrib.auth.models import ContentType
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        email = EmailService(subject='welcome',
                             template_name='mail/welcome.html',
                             to_email=[instance.email])
        email.send()
