from django.urls import path
from . import views

urlpatterns = [
    path('',views.wishlist,name='wishlist'),
    path('add/<int:book_id>/',views.add_to_wishlist,name='add_wishlist')
]
