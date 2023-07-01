class ArticleListRepository:
    articles = []
    article_sequence = 0

    def create_id(self):
        self.article_sequence += 1
        return self.article_sequence

    def save(self, article):
        self.articles.append(article)

    def find_by_id(self, articleId):
        for article in self.articles:
            if article.id == articleId:
                return article
        raise Exception("Article not found")