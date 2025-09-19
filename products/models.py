from django.db import models
CATEGORY_CHOICES = [('fruits','Fruits'),('vegetables','Vegetables'),('dairy','Dairy'),('grains','Grains')]
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='fruits')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
