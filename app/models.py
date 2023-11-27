from django.db import models

# Create your models here.

class VillageData(models.Model):
    Vname=models.CharField(max_length=100)
    Vpname=models.CharField(max_length=100)
    Vjob=models.CharField(max_length=100)
    

    def __str__(self):
        return self.Vname
    

