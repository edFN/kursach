import json

from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from wagtail.fields import StreamField

from blog_app.models import ArticlePage, ArticleReportModel, UserLikesModel
from blog_app.utils import get_client_ip_address


# Create your views here.


class ArticlePageReportAPI(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)

        page_id = request.data.get('page_id', None)

        article_page = get_object_or_404(ArticlePage, pk=page_id)

        block_indexes = request.data.getlist('blocks[]', [])

        blocks_content = article_page.content.raw_data

        report_blocks = [blocks_content[i] for i in range(len(blocks_content)) if str(i) in block_indexes]

        message = request.data.get('message', None)

        email = request.data.get('email', None)

        ArticleReportModel.objects.create(page=article_page,
                                          report_items=json.dumps(report_blocks),
                                          email=email,
                                          message=message)

        return Response(status=200)


class LikeArticeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        article_id = request.data.get('page_id')

        article_instance = get_object_or_404(ArticlePage, pk=article_id)

        remote_addr = get_client_ip_address(request)

        print(remote_addr)

        item, created = UserLikesModel.objects.get_or_create(user_ip=remote_addr, article=article_instance)

        print("Created",created)

        if not created and item.is_active:
            print("Here1")
            item.is_active = False
            item.save()
        elif not item.is_active:
            print("Here2")
            item.is_active=True
            item.save()

        return Response(status=200)
