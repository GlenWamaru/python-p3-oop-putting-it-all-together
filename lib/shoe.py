# lib/shoe.py

class Shoe:
    def __init__(self, brand, size, color, price):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.condition = "New"

    def get_brand(self):
        return self.brand

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def cobble(self):
        self.condition = "New"
        return "The shoe has been repaired."

    def __str__(self):
        return f"{self.brand} {self.color}, Size {self.size}"
