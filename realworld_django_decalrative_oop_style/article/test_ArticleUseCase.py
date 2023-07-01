from unittest import TestCase


from realworld_django_decalrative_oop_style.article.ArticleUseCase import CreateArticle
from realworld_django_decalrative_oop_style.article.repository.ArticleRepository import ArticleListRepository


class UserRepository:
    pass


class TestArticleUseCase(TestCase):
    def setUp(self):
        self.create_article = CreateArticle(ArticleListRepository())

    def test(self):
        article = self.create_article.create(
            CreateArticle.Request(
                "How to train your dragon",
                "Ever wonder how?",
                "You have to believe"
            )
        )
        self.assertEqual("how-to-train-your-dragon", article.slug())
