# Generated by Django 3.1.3 on 2020-11-22 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apartments', '0003_auto_20201121_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='Occupied',
            field=models.BooleanField(default=False),
        ),
    ]