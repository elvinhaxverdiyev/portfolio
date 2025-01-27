from django.contrib import admin
from .models import Home, About, Portfolio
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url1', 'url2', 'url3', 'url4')  
    search_fields = ('name',)  

admin.site.register(Home, HomeAdmin)

admin.site.register(About)
admin.site.register(Portfolio)