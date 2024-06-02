from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock, ListBlock, TextBlock
from wagtail.fields import StreamField
from wagtail.images import get_image_model
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.search import index
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


class ArticleListPage(Page):
    category = models.ForeignKey(CategoryArticle, verbose_name="Категории статей",
                                 null=False, blank=False, on_delete=models.CASCADE)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        articles = ArticlePage.objects.live().public().filter(category=self.category)

        paginator = Paginator(articles, 12)

        page = request.GET.get("page")

        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        context['articles'] = articles

        return context

    content_panels = Page.content_panels + [
        FieldPanel('category')
    ]

    class Meta:
        verbose_name = "Список статей"


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

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('content'),
        index.SearchField('description')
    ]

    def __str__(self):
        return self.title or ''

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class ArticleReportModel(models.Model):
    page = models.ForeignKey(ArticlePage, null=True, blank=True, on_delete=models.CASCADE)
    report_items = StreamField(block_types=[
        ('richtext', RichTextBlock()),
        ('slider_image', SliderImageBlock()),
        ('inform_block', InformBlock()),
        ('table_image', TableImageBlock()),
        ('code', CodeBlock())
    ], null=True,blank=True)
    email = models.EmailField(verbose_name="Емейл отправителя", null=True, blank=True)
    message = models.TextField(verbose_name="Текст замечания", null=True,blank=True)


    panels = [
        FieldPanel('message',read_only=True), FieldPanel('page', read_only=True),
        FieldPanel('report_items'), FieldPanel('email', read_only=True)
    ]

    class Meta:
        verbose_name = "Замечание пользователя"
        verbose_name_plural = "Замечания пользователей"

