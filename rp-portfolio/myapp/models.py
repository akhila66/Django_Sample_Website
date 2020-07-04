from django.db import models

# Create your models here.

class form1(models.Model):
    name = models.CharField(max_length=100)
    number = models.TextField()

class form2(models.Model):
    text1 = models.CharField(max_length=100)
    text2 = models.TextField()

class form3(models.Model):
    text3 = models.CharField(max_length=100)
    text4 = models.TextField()
