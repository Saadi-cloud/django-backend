from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        product = Product.objects.create(name=name, description=description, price=price)
        return render(request, 'product_partial.html', {'product': product})
    return render(request, 'product_form.html')

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        product.name = name
        product.description = description
        product.price = price
        product.save()
        return render(request, 'product_partial.html', {'product': product})
    return render(request, 'product_form.html', {'product': product})


def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return HttpResponse("")
    return render(request, 'product_confirm_delete.html', {'product': product})