# Generated by Django 3.0.2 on 2020-02-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellyoshit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
