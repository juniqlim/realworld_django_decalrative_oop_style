from article2.usecase.domain import ArticleData


class ArticleRepository:
    def save(self, article_data: ArticleData) -> ArticleData:
        pass


class ArticleListRepository(ArticleRepository):
    articles = []
    article_sequence = 0

    def create_id(self):
        self.article_sequence += 1
        return self.article_sequence

    def save(self, article):
        self.articles.append(article)
        return article

    def find_by_slug(self, slug):
        for article in self.articles:
            if article.slug == slug:
                return article
        raise Exception("Article not found")
