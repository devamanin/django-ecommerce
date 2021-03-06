from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4) - (n//4))
    #params = {'no_of_slides':nslides, 'range':range(nslides), 'product':products}
    allProds = [[products, range(1, len(products)), nSlides],
                [products, range(1, len(products)), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at Contact")

def tracker(request):
    return HttpResponse("We are at Tracker")

def search(request):
    return HttpResponse("We are at seach")

def productView(request):
    return HttpResponse("We are at Product View")

def checkout(request):
    return HttpResponse("We are at Checkout")


