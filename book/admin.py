from django.contrib import admin
from . models import GenreModel,BookModel,BorrowModel,BorrowHistoryModel

# Register your models here.
class GenreModelAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('genre_name',)}
    list_display=['genre_name','slug']
admin.site.register(GenreModel,GenreModelAdmin)

class BookModelAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','slug','author','stock']
admin.site.register(BookModel,BookModelAdmin)

class BorrowModelAdmin(admin.ModelAdmin):
    list_display=['user','book','borrow_date','return_date']
admin.site.register(BorrowModel,BorrowModelAdmin)

class BorrowHistoryModelAdmin(admin.ModelAdmin):
    list_display=['user','book','borrow_date','return_date']
admin.site.register(BorrowHistoryModel,BorrowHistoryModelAdmin)