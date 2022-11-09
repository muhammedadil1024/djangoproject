from django.db import models

# Create your models here.
# Registratition Table
class RegTable(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Place = models.CharField(max_length=20)
    Photo = models.ImageField(upload_to ='media/', null = True, blank = True)
    Email = models.EmailField()
    Password = models.CharField(max_length=8)


# Gallery display
class Gallery(models.Model):
    Photos = models.ImageField(upload_to ='media/', null = True, blank = True)
    Name = models.CharField(max_length=20)
    Price = models.IntegerField()
    Brand = models.CharField(max_length=20)
    Year = models.IntegerField()