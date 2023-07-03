from datetime import datetime
from unittest import TestCase

from article2.usecase.test.repository import save, find, remove_all, create_id, find_by_slug
from article2.usecase.usecase import create_article, Request, find_article, ArticleData


class TestArticleData(TestCase):
    def test(self):
        self.assertEqual('title-title', fixture_article().slug)


class TestUseCase(TestCase):
    def test_create_article(self):
        create_article(save, Request(title='title', description='description', body='body'))
        self.assertEquals(1, len(find_article(find)))
        remove_all()


class TestArticleListRepository(TestCase):
    def test_create_id(self):
        self.assertEqual(1, create_id())

    def test_save(self):
        article = fixture_article()

        save(article)
        self.assertEqual(article, find_by_slug('title-title'))
        remove_all()


def fixture_article():
    return ArticleData(slug='Title title'.lower().replace(" ", "-"), title='Title title', description='description',
                       body='body', createdAt=datetime.now(), updatedAt=datetime.now())
