from unittest import TestCase

from article.models import Article


class TestArticle(TestCase):
    def test(self):
        objects_all = Article.objects.all()
        self.assertEqual(0, len(objects_all))
