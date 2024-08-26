from django.urls import path,include
from . import views

app_name = 'job'
urlpatterns = [
    path('books/', views.books_list, name='books_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view, name='library_detail'),
]