articles = []
article_sequence = 0


def create_id():
    global article_sequence
    article_sequence += 1
    return article_sequence


def save(article):
    articles.append(article)
    return article


def find_by_slug(slug):
    for article in articles:
        if article.slug == slug:
            return article
    raise Exception("Article not found")


def find():
    return sorted(articles, key=lambda x: x.createdAt, reverse=True)[:5]


def remove_all():
    global articles
    articles = []
