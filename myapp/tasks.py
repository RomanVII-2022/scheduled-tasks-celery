from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True)
def scheduled_mail(self):
    subject = "Celery"
    message = "This is my first scheduled task"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['victorkinyua12@gmail.com', ]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return "Done"
