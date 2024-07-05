from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from.models import Products
from app_category.models import Category

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Products.objects.filter(category = categories, is_available= True)
        product_count = products.count()
    else:
        products = Products.objects.all().filter(is_available = True).order_by("-modified_date")[:6]
        product_count = products.count()

    return render(request,"app_store/store.html",{
        "product" : products,
        "count" : product_count,
    })

def product_details(request, category_slug, product_slug):
    try:
        single_product = Products.objects.get(category__slug = category_slug, slug = product_slug )
    except Exception as e:
        raise e


    return render(request,"app_store/product_details.html",{
        "single_product" : single_product
    })
    
