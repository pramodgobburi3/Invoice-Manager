from django.db import models
from users.models import *


# Create your models here.
class CompanyProfile(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=10)
    business_phone = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "company_profiles"



