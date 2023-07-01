import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, ArticleSerializer


class ArticleAPI(APIView):
    def get(self, request):
        latest_list = Article.objects.order_by("-createdAt")[:5]
        return Response(ArticleSerializer(latest_list, many=True).data)

    def post(self, request):
        a = request.data.get('article', {})
        return Response(
            ArticleSerializer(
                Article.objects.create(slug=a.get('title').lower().replace(" ", "-"), title=a.get('title'),
                                       description=a.get('description'), body=a.get('body'))
            ).data
        )
