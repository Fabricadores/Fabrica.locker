from django.db import models

# Create your models here.

class rfidTags(models.Model): 
    rfidTag = models.CharField(max_length=10, primary_key=True)
    owner = models.CharField(max_length=50) # this will be the users connection string, received when creating an account at Fabrica.Auth
    def __str__(self):
        return self.rfidTag
    