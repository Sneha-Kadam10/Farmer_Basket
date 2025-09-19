from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CartItem
from products.models import Product
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'Added {product.name} to cart.')
    return redirect('shop')
@login_required
def view_cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum([item.product.price * item.quantity for item in items])
    return render(request, 'cart/cart.html', {'items': items, 'total': total})
@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, user=request.user)
    qty = int(request.POST.get('quantity', 1))
    if qty <= 0:
        item.delete()
    else:
        item.quantity = qty
        item.save()
    return redirect('view_cart')
@login_required
def remove_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, user=request.user)
    item.delete()
    return redirect('view_cart')
@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    items.delete()
    messages.success(request, 'Checkout complete — your order is placed (demo).')
    return redirect('home')
