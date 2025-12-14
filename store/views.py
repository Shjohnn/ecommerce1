from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.db.models import Q
from .models import Product, Category
from .cart import Cart

def home(request):
    query = request.GET.get('q')
    category_slug = request.GET.get('category')
    
    products = Product.objects.filter(is_available=True)

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    
    if category_slug:
        products = products.filter(category__slug=category_slug)

    cart = Cart(request)
    
    # Extra data for UI
    hot_products = Product.objects.filter(is_hot=True).order_by('?')[:3]
    best_sellers = Product.objects.order_by('-sales_count')[:5]
    
    context = {
        'products': products, 
        'cart_len': len(cart),
        'hot_products': hot_products,
        'best_sellers': best_sellers
    }
    return render(request, 'store/home.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    cart = Cart(request)
    
    # Related Products (Same category, excluding current)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id).order_by('?')[:4]
    
    # Sidebar Widget Logic (e.g. Best Sellers)
    sidebar_best_sellers = Product.objects.order_by('-sales_count')[:5]

    context = {
        'product': product,
        'cart_len': len(cart),
        'related_products': related_products,
        'sidebar_best_sellers': sidebar_best_sellers
    }
    return render(request, 'store/product_detail.html', context)

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'store/cart.html', {'cart': cart})
