# Generated by Django 2.1.5 on 2019-02-11 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_issue', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=6)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
            ],
            options={
                'db_table': 'invoices',
                'managed': True,
            },
        ),
    ]
