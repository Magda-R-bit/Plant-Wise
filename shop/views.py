from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/products.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'shop/product_detail.html', {'product': product})


def search_results(request):
    query = request.GET.get('q')
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query) |
        Q(slug__icontains=query)
    ) if query else Product.objects.none()

    return render(request, 'shop/search_results.html', {
        'products': products,
        'query': query
    })
