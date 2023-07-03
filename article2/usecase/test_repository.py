from unittest import TestCase

from article2.usecase.repository import ArticleListRepository
from article2.usecase.test_domain import fixture_article


class TestArticleListRepository(TestCase):
    def test_create_id(self):
        self.assertEqual(1, ArticleListRepository().create_id())

    def test_save(self):
        article_list_repository = ArticleListRepository()
        article = fixture_article()

        article_list_repository.save(article)
        self.assertEqual(article, article_list_repository.find_by_slug('title-title'))
