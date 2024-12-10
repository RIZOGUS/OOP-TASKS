import csv

class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"title {self.title} author {self.author}"

class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages

    def display_info(self):
        info = super().display_info()
        if self.genre and self.pages:
            info += f"genre  {self.genre} pages  {self.pages}"
        return info

class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi

    def display_info(self):
        info = super().display_info()
        if self.journal and self.doi:
            info += f" journal  {self.journal} doi  {self.doi}"
        return info

def save_books(file_name, books):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for book in books:
            writer.writerow([book.title, book.author, book.genre, book.pages])

def save_articles(file_name, articles):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for article in articles:
            writer.writerow([article.title, article.author, article.journal, article.doi])

def read_books(file_name):
    books = []
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    books.append(Book(row[0], row[1], row[2], row[3]))
    except FileNotFoundError:
        pass
    return books

def read_articles(file_name):
    articles = []
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    articles.append(Article(row[0], row[1], row[2], row[3]))
    except FileNotFoundError:
        pass
    return articles

def add_book(file_name, title, author, genre=None, pages=None):
    books = read_books(file_name)
    books.append(Book(title, author, genre, pages))
    save_books(file_name, books)

def add_article(file_name, title, author, journal=None, doi=None):
    articles = read_articles(file_name)
    articles.append(Article(title, author, journal, doi))
    save_articles(file_name, articles)

book_file = "books.csv"
article_file = "articles.csv"

add_book(book_file, "2024", "Muhammad Saifullah", "Civilizations", "200")
add_book(book_file, "Farming", "Muhammad Saifullah")

add_article(article_file, "2024", "Muhammad Saifullah", "Education", "013")
add_article(article_file, 'Driving', "Muhammad Saifullah")

books = read_books(book_file)
for book in books:
    print(book.display_info())

articles = read_articles(article_file)
for article in articles:
    print(article.display_info())
