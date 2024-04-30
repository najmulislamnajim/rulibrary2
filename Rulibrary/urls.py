from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('books/',include('book.urls')),
    path('borrow/',include('borrow.urls')),
    path('wishlist/',include('wishlist.urls')),
    path('review/',include('review.urls')),
    path('accounts/', include('allauth.urls')),
    path('online/',include('book2.urls')),
    path('profile/',views.profile,name='profile'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

