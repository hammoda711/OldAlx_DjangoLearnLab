# Retrieve Operation



Command:
```python
from bookshelf.models import Book

# Retrieving the book we just created
book = Book.objects.get(title="1984")

# Displaying all attributes
print(f"Title: {book.title}, Author: {book.author}, Published Date: {book.published_date}")


Output: Title: 1984, Author: George Orwell, Published Date: 1949-06-08