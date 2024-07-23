from django.contrib import admin

from Product.models import Product, Category, Gender, Brand


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    #readonly_fields = ['slug']
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'price', 'is_published','rating','color']
    list_filter = ['is_published','rating']
    list_editable = ['is_published','color']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Gender)
admin.site.register(Brand)