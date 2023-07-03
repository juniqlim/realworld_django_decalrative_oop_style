from unittest import TestCase

from article2.usecase.repository import ArticleListRepository
from article2.usecase.usecase import create_article, Request


class Test(TestCase):
    def test_create_article(self):
        create_article(ArticleListRepository().save, Request(title='title', description='description', body='body'))
