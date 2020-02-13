from django.db import models

# Create your models here.
class Essay2(models.Model):
   
    name  =models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    language = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    category= models.CharField(max_length=150)
    subcategory = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Essay3(models.Model):
    title =models.CharField(max_length=150)
    lang =models.CharField(max_length=150)
    essay =models.CharField(max_length=20000)

    def __str__(self):
        return self.title