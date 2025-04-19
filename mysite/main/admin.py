from django.contrib import admin
from .models import Categories, Subcategories, Suppliers, Products, UserAddress

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class SubcategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    search_fields = ('name',)
    list_filter = ('category',)

class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'email')
    search_fields = ('name',)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity_in_stock', 'subcategory', 'supplier')
    search_fields = ('name',)
    list_filter = ('subcategory', 'supplier')

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'city', 'state', 'postal_code', 'country')
    search_fields = ('user__username', 'city', 'state')

# Регистрация моделей с настройками
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Subcategories, SubcategoriesAdmin)
admin.site.register(Suppliers, SuppliersAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(UserAddress, UserAddressAdmin)

