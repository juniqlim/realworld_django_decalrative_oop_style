from django.db import models
from rest_framework.serializers import ModelSerializer


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
    from article2.usecase import ArticleData
    return ArticleData(**ArticleSerializer(
        Article.objects.create(slug=article_data.title.lower().replace(" ", "-"), title=article_data.title,
                               description=article_data.description, body=article_data.body)).data)
