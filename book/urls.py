from django.urls import path 
from . import views

urlpatterns = [
    path('',views.books,name='book'),
    path('genre/<slug:genre_slug>/',views.books,name='genre'),
    path('<slug:book_slug>/',views.bookDetails,name='book_details'),
]
