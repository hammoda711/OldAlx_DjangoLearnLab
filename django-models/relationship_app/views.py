from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#function based view
from .models import Book
#class based view
from django.views.generic.detail import DetailView
from .models import Library
#auth views
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

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




def check_admin(user):
    return user.userprofile.role == 'Admin'

def check_librarian(user):
    return user.userprofile.role == 'Librarian'

def check_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(check_member)
def member_view(request):
    return render(request, 'member_view.html')
