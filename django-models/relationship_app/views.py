from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
#function based view
from .models import Book
#class based view
from django.views.generic.detail import DetailView
from .models import Library
#auth views
from django.shortcuts import redirect


# Create your views here.

#function based view

def books_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})



#class based view

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the list of books to the context
        context['books'] = self.object.books.all()
        return context
    


#auth views

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('login')  # Redirect to a login page 
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})
