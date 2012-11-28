from django.db import models

class Concern(models.Model):
   name = models.CharField(max_length=40)

class Employee(models.Model):
   name = models.CharField(max_length=60)
   boss = models.BooleanField(default=False)
   concern = models.ForeignKey(Concern)
   #position = models.CharField(max_length=60)

