# Generated by Django 4.2 on 2023-04-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthor',
            name='biography',
            field=models.TextField(blank=True, verbose_name='biography'),
        ),
    ]
