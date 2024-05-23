from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'category', 'price', 'packet', 'grams', 'stock', 'available')
        }),
        ('Images', {
            'fields': ('image1', 'image2', 'image3')
        }),
    )


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
