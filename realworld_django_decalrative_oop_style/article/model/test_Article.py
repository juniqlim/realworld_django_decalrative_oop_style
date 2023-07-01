from unittest import TestCase

from realworld_django_decalrative_oop_style import Fixture


class TestArticle(TestCase):
    def test_slug(self):
        self.assertEqual("how-to-train-your-dragon", Fixture.article().slug())
