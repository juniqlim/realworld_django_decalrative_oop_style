import json
from unittest import TestCase

import requests


class TestArticleAPI(TestCase):
    def test_get(self):
        response = requests.get('http://127.0.0.1:8000/article2/')
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertFalse(len(json.loads(response.json())['articles']) > 10)

    def test_post(self):
        response = requests.post(
            url='http://127.0.0.1:8000/article2/',
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                "article": {
                    "title": "Article 21",
                    "description": "Description 21",
                    "body": "Content 21"
                }
            })
        )
        print(response.json())
        self.assertEqual(response.status_code, 200)
