class Book:
      def __init__(self, title, author, pages):
            self.title = title
            self.author = author
            self.pages = pages

Book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
Book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)     
print(Book1.title)
print(Book2.title)
print(Book1.author)
print(Book2.author)
print(Book1.pages)
print(Book2.pages)