from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.main_page, name='main'),
    path('company/', views.company_page, name='company'),
    path('faq/', views.faq_page, name='faq'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategory/<int:category_id>/', views.subcategory_list, name='subcategory_list'),
    
    path('login/', views.login_view, name='login'),  # URL для входа
    path('register/', views.register, name='register'),  # URL для регистрации
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # URL для выхода
    
    path('add_address/', views.add_address, name='add_address'),
    path('edit_address/<int:address_id>/', views.edit_address, name='edit_address'),
    path('delete_address/<int:address_id>/', views.delete_address, name='delete_address'),
    
    path('subcategory/<int:subcategory_id>/products/', views.product_list, name='product_list'),
    path('search/', views.search_products, name='search_products'),
    
]