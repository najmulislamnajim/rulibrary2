from django.urls import path
from . import views

urlpatterns = [    
    path('<int:book_id>/',views.borrow,name='borrow'),
    path('borrow_list/',views.borrow_list,name='borrow_list'),
    path('return/<int:book_id>/',views.return_book,name='return'),
    path('multipleError/',views.multiple_try,name='multiple_try_book'),
]
