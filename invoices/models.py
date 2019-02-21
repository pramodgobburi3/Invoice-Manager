from django.db import models
from clients.models import *

# Create your models here.

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_of_issue = models.DateTimeField(auto_now_add=True, blank=True)
    due_date = models.DateTimeField()
    amount_due = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    tax = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = True
        db_table = "invoices"
