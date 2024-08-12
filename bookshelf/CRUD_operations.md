# CRUD Operations

## Create Operation


```python
from bookshelf.models import Book

# Creating a new book instance
book = Book(title="To Kill a Mockingbird", author="Harper Lee", publication_year=1960)
book.save()

# Output
print(book)
# <Book: To Kill a Mockingbird by Harper Lee (1960)>




# Retrieving the book instance just created
book = Book.objects.get(title="To Kill a Mockingbird")

# Output
print(book)
# <Book: To Kill a Mockingbird by Harper Lee (1960)>

# Updating the title of the book
book = Book.objects.get(title="To Kill a Mockingbird")
book.title = "Go Set a Watchman"
book.save()

# Output
print(book)
# <Book: Go Set a Watchman by Harper Lee (1960)>


# Deleting the book instance
book = Book.objects.get(title="Go Set a Watchman")
book.delete()

# Output
# (No output expected, the book is deleted successfully)