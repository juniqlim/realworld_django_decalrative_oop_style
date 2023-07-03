from django.db import models
from rest_framework.serializers import ModelSerializer

from article2.usecase.domain import ArticleData
from article2.usecase.repository import ArticleRepository


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


class ArticleDjangoRepository(ArticleRepository):
    def save(self, article_data):
        return ArticleData(**ArticleSerializer(
            Article.objects.create(slug=article_data.title.lower().replace(" ", "-"), title=article_data.title,
                                   description=article_data.description, body=article_data.body)).data)
