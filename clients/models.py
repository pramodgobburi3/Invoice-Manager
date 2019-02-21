from django.db import models
from company.models import *

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=10)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "clients"


