import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from realworld_django_decalrative_oop_style.article.ArticleUseCase import CreateArticle
from realworld_django_decalrative_oop_style.article.repository.ArticleRepository import ArticleListRepository
from realworld_django_decalrative_oop_style.article.singleton import Singleton


@api_view(['POST'])
def save(request):
    a = request.data.get('article', {})
    create = CreateArticle(Singleton(ArticleListRepository)).create(
        CreateArticle.Request(a.get('title'), a.get('description'), a.get('body')))
    return Response(
        json.dumps(
            create.__dict__
        )
    )


@api_view(['GET'])
def find_by_id(request, article_id):
    singleton = Singleton(ArticleListRepository)
    article = singleton.find_by_id(article_id)
    return Response(
        json.dumps(
            article.__dict__
        )
    )
