from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product, Category
from django.db.models import Q
from .forms import ProductForm


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

def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('shop:add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
