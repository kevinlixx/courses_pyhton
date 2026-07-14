sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_title_traditional(articles):
    """Extrae solo los titulos usando for"""
    titles = []
    for article in articles:
        if len(article["title"]) > 10:
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae solo los titulos usando un comprehension"""
    [article["title"] for article in articles if len(article["title"]) > 10]


def extract_article_summaries(articles):
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["title"]) > 10
    }


def extract_article_sources_traditional(articles):
    """Extrae los source"""
    sources = set()  # el set evita duplicados
    for article in articles:
        # el .get evita errores si no existe la key
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources


def get_sources(articles):
    # {
    # expresion
    # for
    # ifS
    # }
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


def extract_article_sources_comprehensions(articles):
    """Extrae souce con comprehension"""
    return [article["source"] for article in articles]


print(extract_title_traditional(sample_articles))
print("===========")
print(extract_titles(sample_articles))
print("===========")
print(extract_article_sources_traditional(sample_articles))
print("===========")
print(get_sources(sample_articles))
