
from django.db import models

class userInformation(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    account_type = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    
  