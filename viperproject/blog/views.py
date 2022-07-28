from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    #return HttpResponse('Hello World!')
    products = Products.objects.all()
    return render(request, 'index.html', {'items': products})
