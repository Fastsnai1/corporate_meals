# Generated by Django 3.2.18 on 2023-05-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_auto_20230512_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
    ]
