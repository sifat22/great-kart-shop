from django.http import HttpResponse
from django.shortcuts import render
from app_store.models import Products



def home(request):
    products = Products.objects.all().filter(is_available = True)
    return render(request,"home.html",{
       "product" : products,

    })