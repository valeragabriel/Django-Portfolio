from django.db import models

class SideBar(models.Model):
    name = models.CharField(max_length=20)
    anchor = models.CharField(max_length=30, default='')

class Features(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=500)
    img_path = models.ImageField(default='')

class MyProjects(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    img_path = models.ImageField(default='')


