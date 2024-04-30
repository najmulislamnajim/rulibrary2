from django.shortcuts import render,redirect
from book.models import BookModel
from .models import WishlistModel
from django.core.paginator import Paginator

# Create your views here.
def add_to_wishlist(request,book_id):
    if request.user.is_authenticated:
        book=BookModel.objects.get(id=book_id)
        user=request.user
        model_filter=WishlistModel.objects.filter(user=user)
        for item in model_filter:
            if item.book==book:
                return redirect('wishlist')
        
        wishlist, created = WishlistModel.objects.get_or_create(user=user)
        wishlist.book.add(book)
        return redirect('wishlist')
    else:
        return redirect('guest')
    
    
def wishlist(request):
    user=request.user 
    model=WishlistModel.objects.get_or_create(user=user)
    books=None
    model=WishlistModel.objects.filter(user=user)
    for item in model:
        if item.book:
            books=item.book.all()
    page=request.GET.get('page')
    paginator=Paginator(books,9)
    paged_books=paginator.get_page(page)
    return render(request,'wishlist.html',{'data':paged_books})