# Generated by Django 3.1.3 on 2020-11-25 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apartments', '0011_auto_20201124_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenantuser',
            old_name='SSN',
            new_name='Unit',
        ),
        migrations.RemoveField(
            model_name='tenantuser',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='tenantuser',
            name='Username',
        ),
    ]
