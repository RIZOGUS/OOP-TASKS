class Item:
    def __init__(saif, title, author):
        saif.title = title
        saif.author = author

    def displayInfo(saif):
        print(f"Title: {saif.title}, Author: {saif.author}")


class Book(Item):
    def __init__(saif, title, author, pages):
        super().__init__(title, author)
        saif.pages = pages

    def additionalInfo(saif):
        print(f"Pages: {saif.pages}")


class Magazine(Item):
    def __init__(saif, title, author, issueNumber):
        super().__init__(title, author)
        saif.issueNumber = issueNumber

    def additionalInfo(saif):
        print(f"Issue Number: {saif.issueNumber}")


def RegisterItems():
    Book1 = Book("The Alchemist", "Paulo Coelho", 208)
    Book1.displayInfo()
    Book1.additionalInfo()

    Magazine1 = Magazine("National Geographic", "Various", 202)
    Magazine1.displayInfo()
    Magazine1.additionalInfo()

RegisterItems()
