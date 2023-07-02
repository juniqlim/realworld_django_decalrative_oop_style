from dataclasses import dataclass
from datetime import datetime

from article2.models import save


def create_article(request):
    return save(ArticleData(slug=request.title.lower().replace(" ", "-"), title=request.title,
                            description=request.description, body=request.body, createdAt=datetime.now(),
                            updatedAt=datetime.now()))


@dataclass
class Request:
    title: str
    description: str
    body: str


@dataclass
class ArticleData:
    slug: str
    title: str
    description: str
    body: str
    createdAt: str
    updatedAt: str
