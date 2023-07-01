import unittest
from typing import Optional


class Singleton:
    _instance = {}

    def __new__(self, cls, *args, **kwargs):
        if cls.__name__ not in self._instance:
            self._instance[cls.__name__] = cls(*args)
        return self._instance[cls.__name__]

    @staticmethod
    def remove_all():
        Singleton._instance = {}


class ArticleRepository:
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)

    def __init__(self, status: Optional[int] = None):
        self._status = status
        print("init")

    def status(self):
        return self._status


class TestSingleton(unittest.TestCase):
    def test(self):
        Singleton.remove_all()
        repo1 = Singleton(ArticleRepository, 1)
        repo2 = Singleton(ArticleRepository, 2)

        self.assertTrue(repo1 is repo2)
        self.assertEqual(1, repo1.status())
        self.assertEqual(1, repo2.status())

    def test2(self):
        singleton = Singleton
        singleton.remove_all()
        repo1 = Singleton(ArticleRepository)
        repo2 = Singleton(ArticleRepository)

        self.assertTrue(repo1 is repo2)
        self.assertEqual(None, repo1.status())
        self.assertEqual(None, repo2.status())
