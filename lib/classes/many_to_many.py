class Article:
    all = []

    def __init__(self, author, magazine, title):
        
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            
            self._title = None
        else:
            self._title = title

        
        if not isinstance(author, Author):
            
            self._author = None
        else:
            self._author = author

        
        if not isinstance(magazine, Magazine):
            
            self._magazine = None
        else:
            self._magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        
        # raise Exception("Cannot modify title")
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            
            raise Exception("Author name must be a non-empty string")
            self._name = None
        else:
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        #raise Exception("Cannot change author name")
        pass

    def articles(self):
        
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        
        magazines = [article.magazine for article in self.articles()]
        
        seen = set()
        unique_magazines = []
        for mag in magazines:
            if mag not in seen:
                unique_magazines.append(mag)
                seen.add(mag)
        return unique_magazines

    def add_article(self, magazine, title):
        
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        
        seen = set()
        areas = []
        for mag in mags:
            if mag.category not in seen:
                areas.append(mag.category)
                seen.add(mag.category)
        return areas


class Magazine:
    all = []

    def __init__(self, name, category):
        
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            
            raise Exception("Magazine name must be string 2-16 chars")
            self._name = None
        else:
            self._name = name

        
        if not isinstance(category, str) or len(category) == 0:
            
            self._category = None
        else:
            self._category = category

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and (2 <= len(value) <= 16):
            self._name = value
        

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value


    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        
        seen = set()
        unique_authors = []
        for author in authors:
            if author not in seen:
                unique_authors.append(author)
                seen.add(author)
        return unique_authors

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [article.title for article in arts]

    def contributing_authors(self):
        
        authors = self.contributors()
        contributing = []
        for author in authors:
            count = sum(1 for article in self.articles() if article.author == author)
            if count > 2:
                contributing.append(author)
        if len(contributing) == 0:
            return None
        return contributing

   


