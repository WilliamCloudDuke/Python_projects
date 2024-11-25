# Basic class definitions


# TODO: create a basic class
class Book:
  def __init__(self, title): # this is the class constructor
    self.title = title
     

# TODO: create instances of the class
book1 = Book("Brave new word") # automatically calls init() function of Book's class
book2 = Book("War and peace")

# TODO: print the class and property
print(book1.title)
print(book2.title)