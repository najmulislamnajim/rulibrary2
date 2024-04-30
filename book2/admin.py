from django.contrib import admin
from .models import OnlineBookModel

# Register your models ha
class OnlineBookModelAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','author']
admin.site.register(OnlineBookModel,OnlineBookModelAdmin)