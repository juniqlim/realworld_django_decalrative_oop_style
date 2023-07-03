from dataclasses import dataclass


@dataclass
class ArticleData:
    slug: str
    title: str
    description: str
    body: str
    createdAt: str
    updatedAt: str
