from django.db import models
from django.contrib.auth.models import User 
from book.models import BookModel

# Create your models here.
class ReviewModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    rating=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    comment=models.TextField()
    
    def __str__(self):
        return str(self.user)