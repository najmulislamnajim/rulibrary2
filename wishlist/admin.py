from django.contrib import admin
from . models import WishlistModel

# Register your models here.
class WishlistModelAdmin(admin.ModelAdmin):
    list_display=['user']
admin.site.register(WishlistModel,WishlistModelAdmin)