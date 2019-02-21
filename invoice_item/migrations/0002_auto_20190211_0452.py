# Generated by Django 2.1.5 on 2019-02-11 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice_item', '0001_initial'),
        ('invoices', '0001_initial'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.Invoice'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
    ]
