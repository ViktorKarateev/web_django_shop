from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Product
from .forms import ProductForm

def home(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 6)  # 6 товаров на страницу

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/home.html', {'page_obj': page_obj})

def contacts(request):
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(f"[ОБРАТНАЯ СВЯЗЬ] Имя: {name}, Сообщение: {message}")
        success = True

    return render(request, 'catalog/contacts.html', {'success': success})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')  # перенаправим на главную
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})
