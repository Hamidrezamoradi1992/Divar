from time import sleep
from celery import shared_task

from service.email import EmailService


@shared_task
def send_email(subject, template_name, to_email, context):
    email = EmailService(
        subject=subject,
        template_name=template_name,
        to_email=to_email,
        context=context
    )
    print(f"SEND{context} {to_email}")
    email.send()
    print(f"COMPILED {context} {to_email}")

