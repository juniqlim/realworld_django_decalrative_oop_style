from django.db import models
from rest_framework.serializers import ModelSerializer

from article2.usecase.usecase import ArticleData


class Article(models.Model):
    slug = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['slug', 'title', 'description', 'body', 'createdAt', 'updatedAt']


def save(article_data):
    return ArticleData(**ArticleSerializer(
        Article.objects.create(slug=article_data.slug, title=article_data.title,
                               description=article_data.description, body=article_data.body)).data)


def find():
    return [ArticleData(**ArticleSerializer(article).data) for article in Article.objects.order_by("-createdAt")[:5]]
