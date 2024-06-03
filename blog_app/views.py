import json

from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from wagtail.fields import StreamField

from blog_app.models import ArticlePage, ArticleReportModel


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
