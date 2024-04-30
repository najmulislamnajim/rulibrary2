from django.db import models
from book.models import GenreModel

# Create your models here.
class OnlineBookModel(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True)
    author=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/onlinebooks')
    language=models.CharField(max_length=50)
    gdrive=models.CharField(max_length=200)
    genre=models.ManyToManyField(GenreModel)
    
    def __str__(self):
        return f'{self.name} - {self.author}'
    