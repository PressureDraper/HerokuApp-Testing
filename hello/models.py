from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class users(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=254, null=False)
    reason = models.CharField(max_length=254, unique=True, null=False)
    use = models.CharField(max_length=254, null=False)
    date = models.CharField(max_length=30, null=False)
    hour = models.CharField(max_length=30, null=False)
    phone = models.BigIntegerField(null=False)

class testing(models.Model):
    username = models.CharField(max_length=30, null=False)
    pwd = models.CharField(max_length=30, null=False)
