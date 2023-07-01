from unittest import TestCase

from realworld_django_decalrative_oop_style import Fixture


class TestArticle(TestCase):
    def test(self):
        self.assertEqual("How to train your dragon", Fixture.article().title)


if __name__ == '__main__':
    TestCase.main()
