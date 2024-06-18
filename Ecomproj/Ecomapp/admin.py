from django.contrib import admin
from Ecomapp.models import Category
from Ecomapp.models import Product            #  (or)  from . models import *
from Ecomapp.models import *
# Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','image','description']
# admin.site.register(Category,CategoryAdmin)

# class ProAdmin(admin.ModelAdmin):
#     product_display = ['name','product_image','description']
# # admin.site.register(Product,ProductAdmin)
    
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)