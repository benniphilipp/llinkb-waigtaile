# Generated by Django 4.2.6 on 2023-11-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='headline',
            field=models.CharField(blank=True, max_length=350, verbose_name='Überschrift'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subline',
            field=models.CharField(blank=True, max_length=350, verbose_name='Unterzeile'),
        ),
    ]
