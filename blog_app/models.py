from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock, ListBlock, TextBlock
from wagtail.fields import StreamField
from wagtail.images import get_image_model
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtailcodeblock.blocks import CodeBlock

from shared.blocks import SliderImageBlock, InformBlock, TableImageBlock


# Create your models here.

class CategoryArticle(models.Model):
    title = models.CharField("Название категории", max_length=128)

    class Meta:
        verbose_name = 'Категория статьи'
        verbose_name_plural = "Категории статей"

    def __str__(self):
        return self.title or ''


class ArticlePage(Page):
    description = models.TextField(verbose_name="Описание", null=True, blank=False)

    category = ParentalManyToManyField(CategoryArticle, verbose_name="Категории статьи",
                                      null=True, blank=True)

    image_card = models.ForeignKey(get_image_model(), null=True, blank=True, on_delete=models.SET_NULL)

    content = StreamField(block_types=[
        ('richtext', RichTextBlock()),
        ('slider_image', SliderImageBlock()),
        ('inform_block', InformBlock()),
        ('table_image', TableImageBlock()),
        ('code', CodeBlock())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'), FieldPanel('category'), FieldPanel('image_card'),
        FieldPanel('content')
    ]

    def __str__(self):
        return self.title or ''

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
