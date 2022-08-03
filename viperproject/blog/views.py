from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

# Create your views here.

def about(request):
    #return HttpResponse('Hello World!')
    from django.core import serializers
    
    products = Products.objects.all()
    data = serializers.serialize('python', products)

    context = {
        'data' : data
    }

    return render(request, 'about.html', context)



