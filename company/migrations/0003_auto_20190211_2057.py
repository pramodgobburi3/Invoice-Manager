# Generated by Django 2.1.5 on 2019-02-11 20:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_remove_client_country'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
        ('company', '0002_remove_comapnyprofile_country'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ComapnyProfile',
            new_name='CompanyProfile',
        ),
    ]
