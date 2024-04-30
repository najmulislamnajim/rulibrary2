from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.book_list,name='online_books'),
    path('read/<int:id>',views.read_book,name='read_book'),
]
