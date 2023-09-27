from django.db import models

# Create your models here.
class testModel(models.Model):
    testText = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")  