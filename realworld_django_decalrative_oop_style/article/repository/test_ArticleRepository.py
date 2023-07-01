from unittest import TestCase

from realworld_django_decalrative_oop_style import Fixture
from realworld_django_decalrative_oop_style.article.repository.ArticleRepository import ArticleListRepository


class TestArticleListRepository(TestCase):
    def test_create_id(self):
        self.assertEqual(1, ArticleListRepository().create_id())

    def test_save(self):
        article_list_repository = ArticleListRepository()
        article_list_repository.save(Fixture.article())
        self.assertEqual(Fixture.article(), article_list_repository.find_by_id(1))

