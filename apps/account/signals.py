from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.account.models import User
from service.email import EmailService

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(type(instance.email))
        email = EmailService(subject='welcome',
                             template_name='mail/welcome.html',
                             to_email=[instance.email])
        email.send()