from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact

# Create your views here.
def contact(request):    
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            