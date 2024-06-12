from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock, ListBlock, TextBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.fields import StreamField
from wagtail.images import get_image_model
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtailcodeblock.blocks import CodeBlock

from blog_app.utils import get_client_ip_address
from shared.blocks import SliderImageBlock, InformBlock, TableImageBlock


# Create your models here.

@register_snippet
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
        ('code', CodeBlock()),
        ('document', ListBlock(DocumentChooserBlock()))
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)


        addr = get_client_ip_address(request)
        #
        try:
            user_like = UserLikesModel.objects.get(article=context['page'], user_ip=addr)
            context['is_liked'] = user_like.is_active
        except:
            context['is_liked'] = False

        try:
            context['likes'] = UserLikesModel.objects.filter(article=context['page'], is_active=True).count()
        except:
            context['likes'] = 0


        print(context)

        return context

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
        ('code', CodeBlock()),
        ('document', ListBlock(DocumentChooserBlock()))
    ], null=True, blank=True)
    email = models.EmailField(verbose_name="Емейл отправителя", null=True, blank=True)
    message = models.TextField(verbose_name="Текст замечания", null=True, blank=True)

    panels = [
        FieldPanel('message', read_only=True), FieldPanel('page', read_only=True),
        FieldPanel('report_items'), FieldPanel('email', read_only=True)
    ]

    class Meta:
        verbose_name = "Замечание пользователя"
        verbose_name_plural = "Замечания пользователей"


class UserLikesModel(models.Model):
    user_ip = models.GenericIPAddressField("Адрес пользователя", null=True, blank=False)
    article = models.ForeignKey(ArticlePage, null=True, blank=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Лайки пользователей"
