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
        fields = '__all__'
