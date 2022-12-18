from django.shortcuts import render

from .models import Smartphone

def index(request):
    smartphone_list = Smartphone.objects.all()
    return render(request, 'products/index.html', {'smartphone_list': smartphone_list})
