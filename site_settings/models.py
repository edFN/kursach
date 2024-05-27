from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.settings.models import BaseGenericSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page

from site_settings.menu.models import Menu


# Create your models here.

class SocialMediaSettingModel(Orderable):
    setting = ParentalKey('SiteSettings', related_name='social_site_settings_rel')
    type = models.CharField("Платформа", max_length=80, choices=(
        ("ВК", "ВК"), ("Youtube", "Youtube"), ('Телеграм', 'Телеграм'),
        ('Одноклассники', 'Одноклассники')
    ))
    link = models.URLField(verbose_name="Ссылка на страницу", null=True, blank=True)

    panel = [FieldPanel('type'), FieldPanel('link')]

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return f'{self.type}{self.pk}'


@register_setting
class SiteSettings(BaseGenericSetting, ClusterableModel):
    title = models.TextField(verbose_name="Название сайта", null=True, blank=False)
    phone = models.CharField(verbose_name="Телефон для связи", max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name="Почта для связи", null=True, blank=True)

    owner_info = models.CharField(verbose_name="ФИО владельца сайта", max_length=80, null=True, blank=True)
    footer_menu = models.ManyToManyField(to=Menu, verbose_name="Меню в подваде", null=True, blank=True,
                                         related_name="footer_menu_rel")

    page_terms_condition = models.ForeignKey(Page, verbose_name="Страница политики и конфенденциальности",
                                             null=True, blank=True, on_delete=models.SET_NULL)

    text_footer = RichTextField(verbose_name='Текст в подвале', null=True,blank=True )

    panels = [
        FieldPanel('title'), FieldPanel('phone'), FieldPanel('email'),
        FieldPanel('owner_info'), FieldPanel('footer_menu'), FieldPanel('page_terms_condition'),
        FieldPanel('text_footer'),
        InlinePanel('social_site_settings_rel', label="Социальные сети")
    ]

    class Meta:
        verbose_name = "Основные настройки сайта"
        verbose_name_plural = "Основные настройки сайта"

    def __str__(self):
        return self.title or ''
