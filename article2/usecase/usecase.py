from dataclasses import dataclass
from datetime import datetime


@dataclass
class ArticleData:
    slug: str
    title: str
    description: str
    body: str
    createdAt: str
    updatedAt: str


def slugify(text):
    return text.lower().replace(" ", "-")


def create_article(save, request):
    return save(ArticleData(slug=slugify(request.title), title=request.title,
                            description=request.description, body=request.body, createdAt=datetime.now(),
                            updatedAt=datetime.now()))


def find_article(find):
    return find()


@dataclass
class Request:
    title: str
    description: str
    body: str
