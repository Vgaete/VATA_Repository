from django.db import models

# Create your models here.
class testModel(models.Model):
    testText = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")  

class Object(models.Model):
    objectName = models.CharField(max_length=25)
    objectCategory = models.CharField(max_length=6)
    objectImage = models.ImageField(upload_to='objectImages/')
    

class Place(models.Model):
    placeName = models.CharField(max_length=25)
    location = models.CharField(max_length=500)
    placeImage = models.ImageField(upload_to='placeImages/')
    placeCategory = models.CharField(max_length=6)