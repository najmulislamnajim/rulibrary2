from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GenreModel(models.Model):
    genre_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    
    def __str__(self):
        return self.genre_name
    
class BookModel(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True)
    author=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='images/books')
    isbn=models.CharField(max_length=50)
    genre=models.ManyToManyField(GenreModel)
    stock=models.IntegerField()
    availability=models.BooleanField(default=True)
    publication_date=models.DateField()
    total_page=models.IntegerField()
    cover=models.CharField(max_length=50,choices=[('paperback','Paper Back'),('hardcover','Hard Cover')])
    language=models.CharField(max_length=50)
    total_borrow=models.IntegerField(default=0)
    total_rating=models.IntegerField(default=0)
    avg_rating=models.IntegerField(default=0)
    
    def availability_status(self):
        if self.stock<=0: 
            self.availability=False
        else:
            self.availability=True
            
    def save(self, *args, **kwargs):
        self.availability_status()
        super().save(*args, **kwargs)
            
    def __str__(self):
        return f'{self.title} - {self.author}'
    
class BorrowModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    borrow_date=models.DateField(auto_now_add=True)
    return_date=models.DateField()
    
    def __str__(self):
        return str(self.user)
    
class BorrowHistoryModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    borrow_date=models.DateField(auto_now_add=True)
    return_date=models.DateField()
    
    def __str__(self):
        return str(self.user)
    
    