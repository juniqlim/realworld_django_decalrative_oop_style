from dataclasses import dataclass
from datetime import datetime

from article2.usecase.domain import ArticleData


def create_article(save, request):
    return save(ArticleData(slug=request.title.lower().replace(" ", "-"), title=request.title,
                            description=request.description, body=request.body, createdAt=datetime.now(),
                            updatedAt=datetime.now()))


@dataclass
class Request:
    title: str
    description: str
    body: str
