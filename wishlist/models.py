from django.db import models
from django.contrib.auth.models import User 
from book.models import BookModel

# Create your models here.
class WishlistModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ManyToManyField(BookModel)
    
    def __str__(self):
        return str(self.user)