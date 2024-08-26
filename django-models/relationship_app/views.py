from django.shortcuts import render

# Create your views here.

#function based view
from .models import Book

def books_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})



#class based view
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the list of books to the context
        context['books'] = self.object.books.all()
        return context