from django.shortcuts import render, redirect
from .models import Property

# Create your views here.
def addProperties(request):

    return render(request, 'properties/add_properties.html')


def viewProperty(request):
    properties = Property.objects.all()
    
    context ={
        'properties' : properties
    }

    return render(request, 'properties/properties.html', context)
