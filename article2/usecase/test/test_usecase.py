from unittest import TestCase

from article2.usecase.repository import save, find, remove_all
from article2.usecase.usecase import create_article, Request, find_article


class Test(TestCase):
    def test_create_article(self):
        create_article(save, Request(title='title', description='description', body='body'))
        self.assertEquals(1, len(find_article(find)))
        remove_all()
