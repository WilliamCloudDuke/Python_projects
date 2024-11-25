# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "this is a secret attibute" # __atribute is to hide attributes from the interpreter 

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount) 
        else:
            return self.price

    def setDiscount(self, amount):
        self._discount = amount #_discount to tell other programmers this is a private variable and should bnot be used elsewhere

    def getTitle(self):
        return self.title

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print("the price of book: ", b1.getTitle(), " is: ", float(b1.getPrice()))

# TODO: try setting the discount
print(b2.getPrice())
b2.setDiscount(0.25)
#############################
print(b2.getPrice())


# TODO: properties with double underscores are hidden by the interpreter
#print("secret attribute: ", b1.__secret)
print("secret attribute: ", b2._Book__secret) ## you can access it by using class name