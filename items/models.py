from django.db import models
from company.models import *

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "items"