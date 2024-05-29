from django.db import models
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet


# Create your models here.

@register_snippet
class SnippetRegisterForm(models.Model):
    title = models.TextField(verbose_name="Название", null=True, blank=True)
    text = RichTextField(verbose_name="Текст", null=False, blank=True)

    text_success = RichTextField(verbose_name="Текст успешной регистрации Email",
                                 null=False, blank=True)

    class Meta:
        verbose_name = "Блок приема Email пользователя"

    def __str__(self):
        return self.title or ''


class NotificationEmailRegister(models.Model):
    email = models.EmailField("Email пользователя", null=True, blank=False, unique=True)

    class Meta:
        verbose_name = "Электронная почта"
        verbose_name_plural = "Электронная почта для рассылки"

    def __str__(self):
        return self.email or ''
