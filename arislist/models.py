from django.db import models


# Create your models here.


class Classified(models.Model):
    Name = models.CharField(max_length=200)
    Model_Name = models.CharField(max_length=10)
    Date_Created = models.DateTimeField('Date published')
    Price = models.IntegerField(default=0)


class Product(models.Model):
    Model_Name = models.ForeignKey(Classified.Model_Name)
    Version = models.IntegerField(default=0)
