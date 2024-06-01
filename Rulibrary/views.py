from django.shortcuts import render
from book.models import GenreModel,BookModel
from book2.models import OnlineBookModel
from contact.forms import ContactForm

def home(request):
    genres=GenreModel.objects.all()
    if request.method=='POST':
        search_field=request.POST.get('search_field')
        print('vai vai',search_field is None)
        results=BookModel.objects.filter(title__icontains=search_field)
        result=OnlineBookModel.objects.filter(name__icontains=search_field)
        if results is not None:
            return render(request,'search_results.html',{'results':results,'result':result})
        
        
    books=BookModel.objects.filter(availability=True)[:9]
    obooks=OnlineBookModel.objects.all()
    genres=GenreModel.objects.all()
    

    
    
    context={'books':books,'obooks':obooks,'genres':genres}
    return render(request,'base.html',context)

def profile(request):
    return render(request,'profile.html')

