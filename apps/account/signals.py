from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.account.models import User
from service.email import EmailService
from apps.core.models.images import Image
from django.contrib.auth.models import ContentType
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        content=ContentType.objects.get(model='user')
        Image.objects.get_or_create(alt='user_image',
                                    instance_id=instance.id,
                                    name=instance.email,
                                    content_type=content)
        print(type(instance.email))
        email = EmailService(subject='welcome',
                             template_name='mail/welcome.html',
                             to_email=[instance.email])
        email.send()
