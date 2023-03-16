from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')  # ищем в запросе параметр sort, если его нет - устанавливаем его в name
    # сортируем по возрастанию, убыванию цены и по названию
    if sort == 'min_price':
        p = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        p = Phone.objects.all().order_by('-price')
    else:
        p = Phone.objects.all().order_by(sort)
    context = {"phones": p}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # фильтр базы данных по slug (а он эксклюзивный), [0] - первый элемент списка
    # (а список всегда из 1 элемента, т.к. slug - эксклюзивный)
    prod = Phone.objects.filter(slug=slug)[0]
    context = {"phone": prod}
    return render(request, template, context)
