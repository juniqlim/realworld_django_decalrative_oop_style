from realworld_django_decalrative_oop_style.article.model.Article import Article


class CreateArticle:
    def __init__(self, article_repository):
        self.article_repository = article_repository

    def create(self, request) -> Article:
        article = Article(self.article_repository.create_id(), request.title, request.description, request.body)
        self.article_repository.save(article)
        return article

    class Request:
        def __init__(self, title, description, body):
            self.title = title
            self.description = description
            self.body = body


class FindArticle:
    def __init__(self, article_repository):
        self.article_repository = article_repository

    def find_by_id(self, request) -> Article:
        return self.article_repository.find_by_id(request.articleId)

    class Request:
        def __init__(self, articleId):
            self.id = articleId
