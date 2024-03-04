# lib/book.py

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_title(self):
        return self.title

    def get_pages(self):
        return self.pages

    def get_price(self):
        return self.price

    def turn_page(self):
        return "Flipping the page...wow, you read fast!"

    def __str__(self):
        return f"{self.title}"
