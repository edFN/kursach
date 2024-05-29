from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField, RichTextField

from wagtail.models import Page

from shared.blocks import SliderPageBlock, TableCardBlock, InformBlock


class EmptyPage(Page):
    pass


class HomePage(Page):
    content = StreamField([
        ('richtext', RichTextBlock()),
        ('slider_page', SliderPageBlock()),
        ('table_page', TableCardBlock()),
        ('inform_block', InformBlock()),
    ], null=True, blank=True, verbose_name="Содержимое")

    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    class Meta:
        verbose_name = "Главная страница"
