from django.db import models

# Create your models here.

class user_master(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    mobile = models.CharField(max_length=40)
    role = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.username
    

class contact_master(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    message = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.name