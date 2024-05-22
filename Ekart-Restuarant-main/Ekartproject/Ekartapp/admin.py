from django.contrib import admin

# Register your models here.
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


# class ProductAdmin(admin.ModelAdmin):
#     # list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
#     # list_editable = ['price', 'stock', 'available']
#     prepopulated_fields = {'slug': ('name',)}
#     list_per_page = 20
#
#
# admin.site.register(Product, ProductAdmin)



# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'available', 'created', 'updated']
#     list_filter = ['available', 'created', 'updated']
#     list_editable = ['available']
#     prepopulated_fields = {'slug': ('name',)}

from django.contrib import admin
from .models import Category, Product, PacketSize

class PacketSizeInline(admin.TabularInline):
    model = PacketSize
    extra = 1

class ProductAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    # list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    # list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
=======
    inlines = [PacketSizeInline]
>>>>>>> d4c4eead28b5a93d352fb1a0951df745ce6bed89


admin.site.register(Product, ProductAdmin)



# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'available', 'created', 'updated']
#     list_filter = ['available', 'created', 'updated']
#     list_editable = ['available']
#     prepopulated_fields = {'slug': ('name',)}

# from django.contrib import admin
# from .models import Category, Product, PacketSize
#
# class PacketSizeInline(admin.TabularInline):
#     model = PacketSize
#     extra = 1
#
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [PacketSizeInline]
#
#
# admin.site.register(Product, ProductAdmin)
