from article2.usecase.domain import ArticleData
from article2.models import ArticleSerializer, Article


def save(article_data):
    return ArticleData(**ArticleSerializer(
        Article.objects.create(slug=article_data.title.lower().replace(" ", "-"), title=article_data.title,
                               description=article_data.description, body=article_data.body)).data)
