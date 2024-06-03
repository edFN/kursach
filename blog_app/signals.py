from django.conf import settings
from django.core.mail import send_mail
from wagtail.signals import page_published

from blog_app.models import ArticlePage
from notification_app.models import NotificationEmailRegister


def publish_users_email(sender, **kwargs):
    emails = NotificationEmailRegister.objects.all().values_list('email', flat=True)

    send_mail("Оповещение!", f"Скорее читайте новый пост {kwargs['instance'].title}",
                  settings.DEFAULT_FROM_EMAIL, emails, fail_silently=False)


page_published.connect(publish_users_email, sender=ArticlePage)
