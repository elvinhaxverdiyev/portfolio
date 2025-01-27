from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_pics/')  # Resimlerin yükleneceği klasör
    rol1 = models.CharField(max_length=20, null=True, blank=True)
    rol2 = models.CharField(max_length=20, null=True, blank=True)
    rol3 = models.CharField(max_length=20, null=True, blank=True)
    url1 = models.URLField(blank=True, null=True)  
    url2 = models.URLField(blank=True, null=True)  
    url3 = models.URLField(blank=True, null=True)  
    url4 = models.URLField(blank=True, null=True)  

    def __str__(self):
        return self.name




class About(models.Model):
    title = models.CharField(max_length=250)
    position = models.TextField()
    text = models.TextField()
    birthday = models.DateField()
    profil_image = models.ImageField(upload_to='profile_pics/', null=True)
    phone = models.IntegerField()
    city = models.TextField()
    mission = models.TextField(max_length=200, blank=True, null=True)
    age = models.IntegerField()
    degree = models.TextField()
    mail = models.EmailField()
    freelencer = models.TextField(default='Freelance information not available')

    def __str__(self):
        return self.title

