"""
URL configuration for realworld_django_decalrative_oop_style project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import admin
from django.urls import path

from realworld_django_decalrative_oop_style.article.web import ArticleController


class IndexView(APIView):
    def get(self, request):
        return Response({'hello': 'world'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('articles', ArticleController.save, name='save'),
    path('articles/<int:article_id>', ArticleController.find_by_id, name='find_by_id'),
]
