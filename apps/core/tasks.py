from time import sleep
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from apps.advertising.models import Advertising
from django.utils import timezone


@shared_task
def send_email(subject, to_email, context, template_name=None):
    subject = subject
    message = context
    recipient_list = to_email
    print(f"SEND{context} {to_email}")
    send_mail(subject, message, None, recipient_list)
    print(f"COMPILED {context} {to_email}")


@shared_task
def expire_at_advertise():
    advertise = Advertising.objects.filter(diffusion=True, expires_at__lt=timezone.now())
    advertise_email = list(advertise.values_list('user__email', 'title'))
    advertise.update(is_active=False, is_deleted=True,diffusion=False)
    for email, title in advertise_email:
        send_email.delay(subject='expire at advertise', to_email=[email],
                         context=f'your advertise by name {title} in out one monte expire at in wall')
    print("COMPILED")

# print(f"SEND{context} {to_email}")
# send_mail(subject=subject,message=context,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=to_email)
# print(f"COMPILED {context} {to_email}")

# def send_simple_email():
# subject = "Test Email from Django"
# message = "This is a test email sent from a Django project."
# recipient_list = ["recipient@example.com"]
#
# try:
# send_mail(subject, message, None, recipient_list)
