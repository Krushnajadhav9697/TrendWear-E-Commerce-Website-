from django.contrib import admin
from .models import Category,Product

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','description']

admin.site.register(Category,categoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','description','category','gender']
    
admin.site.register(Product,ProductAdmin)



