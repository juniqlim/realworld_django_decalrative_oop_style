from unittest import TestCase

from article2.usecase.repository import create_id, save, find_by_slug, remove_all
from article2.usecase.test.test_domain import fixture_article


class TestArticleListRepository(TestCase):
    def test_create_id(self):
        self.assertEqual(1, create_id())

    def test_save(self):
        article = fixture_article()

        save(article)
        self.assertEqual(article, find_by_slug('title-title'))
        remove_all()
