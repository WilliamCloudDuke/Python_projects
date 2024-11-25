# Using the __str__ and __repr__ magic methods


from typing import Any


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):  #this method is the same as the toString() in Java
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: the __call__ method can be used to call the object like a function
    def __call__(self,title, author, price):
        self.author = author
        self.price = price
        self.title = title


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# TODO: call the object as if it were a function
b1("the lord of the rings", "William Chaparro", 34.00)
print(b1) # overrode the propertie of object b1 entirely 