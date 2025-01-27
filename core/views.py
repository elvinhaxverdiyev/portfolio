from django.shortcuts import render
from .models import Home, About

def home(request):
    home_items = Home.objects.all() 
    about_item = About.objects.first() 

    return render(request, 'home.html', {'home_items': home_items, 'about_item': about_item})
