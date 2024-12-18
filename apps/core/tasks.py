from time import sleep
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email(subject, to_email, context,template_name=None):
        subject = subject
        message = context
        recipient_list = to_email
        print(f"SEND{context} {to_email}")
        send_mail(subject, message, None, recipient_list)
        print(f"COMPILED {context} {to_email}")



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