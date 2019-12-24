from django.urls import path
from . import views

urlpatterns = [
    # Calls the view function that is a function named index() in views.py file 
    path('', views.index, name='index'),
    # URL mapper for Book List View
    path('books/', views.BookListView.as_view(), name='books'),
    # URL mapper for Book Detail View
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]