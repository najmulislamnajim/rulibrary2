from django.shortcuts import render,get_object_or_404,redirect
from .models import GenreModel,BorrowModel,BookModel
from django.core.paginator import Paginator
from review.models import ReviewModel

# Create your views here.
def books(request,genre_slug=None):
    # ========> Search Start <=============
    if request.method=='POST':
        search_field=request.POST.get('search_field')
        results=BookModel.objects.filter(title__icontains=search_field)
        if results is not None:
            return render(request,'search_results.html',{'results':results})
    # ========> Search End <=============
        
    if genre_slug:
        genre=get_object_or_404(GenreModel,slug=genre_slug)
        books=BookModel.objects.filter(availability=True,genre=genre)
    else:
        books=BookModel.objects.filter(availability=True)
    genres=GenreModel.objects.all()
    
    page=request.GET.get('page')
    paginator=Paginator(books,6)
    paged_book=paginator.get_page(page)
    
    contex={'books':paged_book,'genres':genres}
    return render(request,'book_cart.html',contex)

def bookDetails(request,book_slug):
    book=BookModel.objects.get(slug=book_slug)
    reviews=ReviewModel.objects.filter(book=book)
    genres=book.genre.all()
    return render(request,'book_details.html',{'book':book,'genres':genres,'reviews':reviews})



            