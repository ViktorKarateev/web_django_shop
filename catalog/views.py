from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})

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