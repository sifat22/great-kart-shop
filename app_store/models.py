from django.db import models
from app_category.models import Category
from django.urls import reverse

# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    Images = models.ImageField(upload_to='photos/app_products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])
    def __str__(self):
        return self.product_name

