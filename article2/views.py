import json
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import save, find
from .usecase.usecase import create_article, Request, find_article


class ArticleAPI(APIView):
    def get(self, request):
        return Response(
            json.dumps(
                {'articles': [article.__dict__ for article in find_article(find)]},
                default=serialize_datetime
            )
        )

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
