# Update Operation

Command:
```python
from bookshelf.models import Book

# Retrieving the book instance
book = Book.objects.get(title="1984")

# Updating the title
book.title = "Nineteen Eighty-Four"
book.save()

# Displaying the updated book details
print(f"Updated Title: {book.title}")

Output: Updated Title: Nineteen Eighty-Four