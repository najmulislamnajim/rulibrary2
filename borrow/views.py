from django.shortcuts import render,redirect
from django.http import HttpResponse
from book.models import *

# Create your views here.
def multiple_try(request):
    return render(request,'error_message.html')

def borrow(request,book_id):
    if request.user.is_authenticated:
        book=BookModel.objects.get(id=book_id)
        user=request.user
        model_filter=BorrowModel.objects.filter(user=user)
        for item in model_filter:
            if item.book==book:
                return redirect('multiple_try_book')
        
        
        print('printing book',book,book.stock)
        if request.method == 'POST':
            return_date=request.POST.get('return_date')
            user=request.user
            data={
                'user':user,
                'book':book,
                'return_date':return_date
            }
            instance=BorrowModel()
            for key, value in data.items():
                setattr(instance, key, value)
            instance.save()
            book.stock-=1
            book.save()
            return redirect('borrow_list')
            
        return render(request,'borrow_confirmation.html',{'book':book})
    else:
        # return HttpResponse("You need to be logged in to view this page.", status=401)
        return redirect('unauthorized')
    
def borrow_list(request):
    user=request.user
    model=BorrowModel.objects.filter(user=user)    
    return render(request,'borrow-list.html',{'data':model})

def return_book(request,book_id):
    model=BorrowModel.objects.filter(id=book_id)
    for item in model:
        item.book.stock+=1
        item.book.save()
        b_id=item.book.id
    model.delete()
    return redirect('review',book_id=b_id)

def Unauthorized(request):
    return render(request,'berror.html')