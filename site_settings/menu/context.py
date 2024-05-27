from site_settings.menu.models import Menu


def menu_processor(request):
    return {"menu_items": Menu.objects.all()}
