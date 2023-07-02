from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import admin
from django.urls import path, include

from realworld_django_decalrative_oop_style.article.web import ArticleController


class IndexView(APIView):
    def get(self, request):
        return Response({'hello': 'world'})


urlpatterns = [
    path("article/", include("article.urls")),
    path("article2/", include("article2.urls")),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('articles', ArticleController.save, name='save'),
    path('articles/<int:article_id>', ArticleController.find_by_id, name='find_by_id'),
]
