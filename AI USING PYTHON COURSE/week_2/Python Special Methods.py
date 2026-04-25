# Python Special Methods
class book:
    def __init__ (self, title, author):  #__init__ is a special method in Python that is called when an object is created. It is used to initialize the attributes of the object.
        self.title = title
        self.author = author

    def __str__(self):  #__str__ is a special method in Python that is called when you use the print() function on an object. It should return a string representation of the object.
        return f"'{self.title}' by {self.author}"
    
book1 = book("1948", "Harper Lee")
print(book1)  # Output: '1948' by Harper Lee