from django.urls import path

from blog_app.views import ArticlePageReportAPI

urlpatterns = [
    path('', ArticlePageReportAPI.as_view())
]