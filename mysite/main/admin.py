from django.contrib import admin
from .models import Categories, Subcategories, Suppliers, Products, UserAddress, Employee, CartItem, OrderItem, Order

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
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'email', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_active',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    search_fields = ('user__username', 'product__name')
    list_filter = ('user',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address', 'created_at', 'updated_at', 'total_price')  # Добавлено поле id и updated_at
    search_fields = ('user__username', 'address__street')  # Поиск по имени пользователя и адресу
    list_filter = ('created_at', 'user')  # Фильтрация по дате создания и пользователю
    ordering = ('-created_at',)  # Сортировка по дате создания

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')  # Добавлено поле id
    search_fields = ('order__user__username', 'product__name')  # Поиск по имени пользователя и имени продукта
    list_filter = ('order', 'product')  # Фильтрация по заказу и продукту
    ordering = ('order',)  # Сортировка по заказу

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

# Регистрация моделей с настройками
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Subcategories, SubcategoriesAdmin)
admin.site.register(Suppliers, SuppliersAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(CartItem, CartItemAdmin)

# Регистрация моделей с настройками
