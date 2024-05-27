from autoslug import AutoSlugField
from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, PageChooserPanel, MultiFieldPanel, InlinePanel
from wagtail.models import Orderable, Page
from wagtail.snippets.models import register_snippet


class MenuItem(Orderable):
    link_title = models.CharField(blank=True, null=True, max_length=50)
    link_url = models.CharField(max_length=500)
    link_page = models.ForeignKey(Page, null=True, blank=True,
                                  related_name="+", on_delete=models.CASCADE)
    open_in_new_tab = models.BooleanField(default=False)

    page = ParentalKey("Menu", related_name="sub_menu")

    panels = [
        FieldPanel("link_title"),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]


@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from=title, editable=True)

    link_url = models.CharField(max_length=500)
    link_page = models.ForeignKey(Page, null=True, blank=True,
                                  related_name="+", on_delete=models.CASCADE)

    panels = [
        MultiFieldPanel([
            FieldPanel("title"), FieldPanel("slug"), FieldPanel('link_url'), FieldPanel('link_page')
        ], heading="Меню"),
        InlinePanel("sub_menu", label="Menu Item")
    ]

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.title
