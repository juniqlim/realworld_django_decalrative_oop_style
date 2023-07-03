import json
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, ArticleSerializer
from .usecase.repository import save
from .usecase.usecase import create_article, Request


class ArticleAPI(APIView):
    def get(self, request):
        latest_list = Article.objects.order_by("-createdAt")[:5]
        return Response(ArticleSerializer(latest_list, many=True).data)

    def post(self, request):
        return Response(
            json.dumps(
                {'article': create_article(save, Request(**request.data.get('article', {}))).__dict__},
                default=serialize_datetime
            )
        )


def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
