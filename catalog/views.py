from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(f"[ОБРАТНАЯ СВЯЗЬ] Имя: {name}, Сообщение: {message}")
        success = True

    return render(request, 'catalog/contacts.html', {'success': success})