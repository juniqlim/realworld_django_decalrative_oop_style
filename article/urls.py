from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArticleAPI().as_view()),
]
