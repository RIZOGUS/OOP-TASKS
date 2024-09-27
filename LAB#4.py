class Book:
    def __init__(Saif, Title, Author, PublicationYear):
        Saif.Title = Title
        Saif.Author = Author
        Saif.PublicationYear = PublicationYear

    def __str__(Saif):
        return f"Title: {Saif.Title}, Author: {Saif.Author}, Publication Year: {Saif.PublicationYear}"

Book1 = Book("Trust and Inspire", "Stephen Covey", 2022)
print(Book1)
0
