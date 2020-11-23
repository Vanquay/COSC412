# Generated by Django 3.1.3 on 2020-11-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apartments', '0006_bills_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Resolved', models.BooleanField(default=False)),
                ('Issue', models.TextField()),
            ],
        ),
    ]
