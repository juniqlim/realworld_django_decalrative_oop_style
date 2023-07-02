from datetime import datetime

from django.test import TestCase

from .models import Article
from .models import ArticleSerializer


class TestArticle(TestCase):
    def test_create(self):
        create = Article.objects.create(slug='slug', title='title', description='description', body='body')
        self.assertEqual(1, create.id)

    def test_create(self):
        serializer = ArticleSerializer(
            Article.objects.create(slug='slug', title='title', description='description', body='body'))
        self.assertEqual(1, serializer.data['id'])

    def test(self):
        print(datetime.now())
