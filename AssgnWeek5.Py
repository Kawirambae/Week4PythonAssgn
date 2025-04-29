# Base class: Book
class Book:
    

    def __init__(self, title, author, genre, rating):
        self._title = title
        self._author = author
        self._genre = genre
        self._rating = rating

    def display_info(self):
        print(f"📚 '{self._title}' by {self._author} - Genre: {self._genre} - Rating: {self._rating}/5")

# Subclass: Fiction
class Fiction(Book):
    def display_info(self):
        print(f"✨ Fiction: '{self._title}' by {self._author} - {self._rating}/5")

# Subclass: NonFiction
class NonFiction(Book):
    def display_info(self):
        print(f"📘 Non-Fiction: '{self._title}' by {self._author} - {self._rating}/5")

# Program execution starts here
if __name__ == "__main__":
    # Using constructors to create unique book objects
    books = [
        Fiction("The Name of the Wind", "Patrick Rothfuss", "Fantasy", 4.8),
        Fiction("Eragon", "Christopher Paolini", "Fantasy", 4.7),
        NonFiction("Sapiens", "Yuval Noah Harari", "History", 4.6),
        NonFiction("Atomic Habits", "James Clear", "Self-help", 4.5)
    ]

    # Polymorphism in action: 
    print("📚 Book Library:")
    for book in books:
        book.display_info()
