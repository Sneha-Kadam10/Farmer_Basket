from django.shortcuts import render, get_object_or_404
from .models import Product
def shop(request):
    q = request.GET.get('q','').strip()
    category = request.GET.get('category')
    products = Product.objects.all()
    if category:
        products = products.filter(category=category)
    if q:
        products = products.filter(name__icontains=q)
    featured = Product.objects.filter(featured=True)[:8]
    return render(request, 'products/shop.html', {'products': products, 'featured': featured})
def product_detail(request, pk):
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product': p})
