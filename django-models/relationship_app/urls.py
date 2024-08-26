from django.urls import path,include
from . import views 
from .views import list_books

#app_name = 'relationship_app'
urlpatterns = [
    path('books/', views.books_list, name='books_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]