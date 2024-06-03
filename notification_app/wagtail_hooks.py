from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet

from notification_app.models import NotificationEmailRegister
from wagtail.admin.menu import MenuItem

class NotificationEmailViewSet(ModelViewSet):
    model = NotificationEmailRegister
    form_fields = ['email']
    icon = 'form'


@hooks.register("register_admin_viewset")
def register_viewset():
    return NotificationEmailViewSet("submission")

@hooks.register('register_admin_menu_item')
def register_frank_menu_item():
    return MenuItem('Заявки', '/admin/submission', order=1000, icon_name='form')

