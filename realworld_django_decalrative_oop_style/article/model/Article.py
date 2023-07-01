from dataclasses import dataclass


@dataclass
class Article:
    id: int
    title: str
    description: str
    body: str
