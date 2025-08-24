class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author 
        self.magazine = magazine  
        self.title = title  
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("author must be an Author instance.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("magazine must be a Magazine instance.")
        self._magazine = new_magazine

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise AttributeError("Cannot change article's title after it has been set.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = title



class Author:
    def __init__(self, name):
        self.name = name 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change author's name after it has been set.")
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = self.magazines()
        if not topics:
            return None
        return list({topic.category for topic in topics})


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self.name = name  
        self.category = category  
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        art_title = self.articles()
        if not art_title:
            return None
        return [article.title for article in art_title]

    def contributing_authors(self):
        art_title = self.articles()
        if not art_title:
            return None
        author_counts = {}
        for art in art_title:
            author_counts[art.author] = author_counts.get(art.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        top_mag = None
        max_count = 0
        for mag in cls._all_magazines:
            count = len(mag.articles())
            if count > max_count:
                max_count = count
                top_mag = mag
        return top_mag if max_count > 0 else None


