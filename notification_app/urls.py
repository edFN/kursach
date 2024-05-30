from django.urls import path

from notification_app.views import AcceptEmailRegister

urlpatterns = [
    path('email_subscribe', AcceptEmailRegister.as_view())
]