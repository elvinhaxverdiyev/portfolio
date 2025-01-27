from django.shortcuts import render
from .models import Home, About

def home(request):
    home_items = Home.objects.all()  # Home verilerini alıyoruz
    about_item = About.objects.first()  # About modelinin ilk kaydını alıyoruz

    return render(request, 'home.html', {'home_items': home_items, 'about_item': about_item})
