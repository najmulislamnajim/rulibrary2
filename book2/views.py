from django.shortcuts import render,get_object_or_404
from .models import OnlineBookModel
from django.core.paginator import Paginator
from book.models import GenreModel

def book_list(request):
    books = OnlineBookModel.objects.all()
    page=request.GET.get('page')
    paginator=Paginator(books,6)
    paged_book=paginator.get_page(page)
    return render(request, 'online_book.html', {'books': paged_book})

def books(request,genre_slug=None):
    # ========> Search Start <=============
    if request.method=='POST':
        search_field=request.POST.get('search_field')
        results=OnlineBookModel.objects.filter(title__icontains=search_field)
        if results is not None:
            return render(request,'search_results.html',{'results':results})
    # ========> Search End <=============
        
    if genre_slug:
        genre=get_object_or_404(GenreModel,slug=genre_slug)
        books=OnlineBookModel.objects.filter(genre=genre)
    else:
        books=OnlineBookModel.objects.all()
    genres=GenreModel.objects.all()
    
    page=request.GET.get('page')
    paginator=Paginator(books,6)
    paged_book=paginator.get_page(page)
    
    contex={'books':paged_book,'genres':genres}
    return render(request,'online_books.html',contex)

def read_book(request,id):
    book=OnlineBookModel.objects.get(pk=id)
    return render(request, 'online_read.html', {'book':book})
