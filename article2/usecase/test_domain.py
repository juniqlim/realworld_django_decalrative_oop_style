from datetime import datetime
from unittest import TestCase

from article2.usecase.domain import ArticleData


class TestArticleData(TestCase):
    def test(self):
        article = fixture_article()
        self.assertEqual('title-title', article.slug)


def fixture_article():
    return ArticleData(slug='Title title'.lower().replace(" ", "-"), title='Title title', description='description',
                       body='body', createdAt=datetime.now(), updatedAt=datetime.now())
