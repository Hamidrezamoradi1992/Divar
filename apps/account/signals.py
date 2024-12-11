from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.account.models import User
from apps.core.tasks import send_email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        email_data = {
            'subject': 'welcome ',
            'template_name': 'mail/welcome.html',
            'to_email': [instance.email],
            'context': "welcome to wall website",

        }
        send_email.delay(**email_data)


