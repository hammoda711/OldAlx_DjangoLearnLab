from django.urls import path,include
from . import views 
#from .views import list_books
from django.contrib.auth import views as auth_views
#from relationship_app import views  # Import your custom registration view
#app_name = 'relationship_app'
urlpatterns = [
    path('books/', views.books_list, name='books_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
     #auth views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]