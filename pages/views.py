from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product
from .models import ContactMessage
def home(request):
    featured = Product.objects.filter(featured=True)[:8]
    return render(request, 'home.html', {'featured': featured})
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Thanks for contacting us. We will respond soon.')
        return redirect('contact')
    return render(request, 'contact.html')
