from django.urls import path
from . import views

urlpatterns = [
    path('book/',views.book_list,name='online_book'),
    path('books/',views.books,name='online_books'),
    path('genre/<slug:genre_slug>/',views.books,name='online_genre'),
    path('read/<int:id>',views.read_book,name='read_book'),
]
