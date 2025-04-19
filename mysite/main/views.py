from django.shortcuts import get_object_or_404, render, redirect
from .models import Categories, Subcategories, Employee, UserAddress, Products
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserUpdateForm, AddressForm
# # Create your views here.

def main_page(request):
    employees = Employee.objects.filter(is_active=True)  # Извлекаем только активных сотрудников
    return render(request, 'main/main.html', {'employees': employees})

def company_page(request):
    return render(request, 'main/company.html')

def faq_page(request):
    return render(request, 'main/faq.html')

def contacts_page(request):
    return render(request, 'main/contacts.html')

def category_list(request):
    categories = Categories.objects.all()
    products = Products.objects.all()  # Получаем все товары
    return render(request, 'main/category_list.html', {
        'categories': categories,
        'products': products
    })

def subcategory_list(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    subcategories = Subcategories.objects.filter(category=category)  # Получаем подкатегории для выбранной категории
    products = Products.objects.filter(subcategory__category=category)  # Получаем товары, принадлежащие выбранной категории
    return render(request, 'main/subcategory_list.html', {
        'category': category,
        'subcategories': subcategories,
        'products': products
    })
    
def product_list(request, subcategory_id):
    subcategory = get_object_or_404(Subcategories, id=subcategory_id)
    products = Products.objects.filter(subcategory=subcategory)  # Получаем товары для выбранной подкатегории
    return render(request, 'main/product_list.html', {
        'subcategory': subcategory,
        'products': products
    })
    
def search_products(request):
    query = request.GET.get('q')
    if query:
        products = Products.objects.filter(name__icontains=query)  # Поиск по имени товара
    else:
        products = Products.objects.none()  # Если нет запроса, возвращаем пустой QuerySet

    return render(request, 'main/search_results.html', {'products': products, 'query': query})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем нового пользователя
            login(request, user)  # Входим в систему автоматически
            return redirect('user_profile')  # Перенаправляем на личный кабинет
    else:
        form = UserCreationForm()  # Создаем пустую форму для регистрации
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Входим в систему
                return redirect('user_profile')  # Перенаправляем на личный кабинет
    else:
        form = AuthenticationForm()  # Создаем пустую форму для входа
    return render(request, 'main/login.html', {'form': form})

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'main/user_profile.html', {
        'user': request.user,
        'form': form
    })

@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('user_profile')
    return redirect('user_profile')

@login_required
def edit_address(request, address_id):
    address = get_object_or_404(UserAddress, id=address_id, user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    return redirect('user_profile')

@login_required
def delete_address(request, address_id):
    address = get_object_or_404(UserAddress, id=address_id, user=request.user)
    address.delete()
    return redirect('user_profile')