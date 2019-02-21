from django.db import models
from items.models import *
from invoices.models import *

# Create your models here.
class InvoiceItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "invoice_items"
