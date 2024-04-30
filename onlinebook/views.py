from django.shortcuts import render
from .models import OnlineBookModel
from django.core.paginator import Paginator

def book_list(request):
    books = OnlineBookModel.objects.all()
    page=request.GET.get('page')
    paginator=Paginator(books,6)
    paged_book=paginator.get_page(page)
    return render(request, 'online_book.html', {'books': paged_book})

def read_book(request,id):
    book=OnlineBookModel.objects.get(pk=id)
    return render(request, 'online_read.html', {'book':book})
