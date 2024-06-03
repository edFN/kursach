from django.core.exceptions import ImproperlyConfigured
from django.forms import Form, modelform_factory
from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet

from .models import ArticleReportModel

from wagtail.admin.menu import MenuItem


class ReportViewSet(ModelViewSet):
    model = ArticleReportModel
    # form_fields = '__all__'
    icon = 'form'


@hooks.register("register_admin_viewset")
def register_viewset():
    return ReportViewSet("reports")


@hooks.register('register_admin_menu_item')
def register_frank_menu_item():
    return MenuItem('Заявки на исправления', '/admin/reports', order=1000, icon_name='form')
