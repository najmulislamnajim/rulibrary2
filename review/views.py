from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .forms import ReviewForm
from .models import ReviewModel
from book.models import BookModel

# Create your views here.
def review(request,book_id=1):
    print(book_id)
    form=ReviewForm
    book=get_object_or_404(BookModel,id=book_id)
    user_review=ReviewModel.objects.filter(user=request.user,book=book).first()
    if user_review:
        return redirect('home')
    else:    
        if request.method=='POST':
            print('vai ekhane')
            form=ReviewForm(request.POST)
            if form.is_valid() and not user_review:
                print('vai vai ekhane')
                rating=form.cleaned_data['rating']
                comment=form.cleaned_data['comment']
                review=ReviewModel.objects.create(
                    user=request.user,
                    book=book,
                    rating=rating,
                    comment=comment
                )
                return redirect('home')
                
        return render(request,'review.html',{'form':form})