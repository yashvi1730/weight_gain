# Generated by Django 3.0.7 on 2020-07-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200717_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(blank=True, default=False, null=True),
        ),
    ]