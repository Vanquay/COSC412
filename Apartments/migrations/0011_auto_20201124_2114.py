# Generated by Django 3.1.3 on 2020-11-25 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apartments', '0010_auto_20201124_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorders',
            name='Resolved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='workorders',
            name='Issue',
            field=models.TextField(),
        ),
    ]
