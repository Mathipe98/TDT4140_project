# Generated by Django 3.0.2 on 2020-03-13 15:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objectviewed',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Object viewed',
                     'verbose_name_plural': 'Objects viewed'},
        ),
    ]
