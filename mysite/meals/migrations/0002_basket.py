# Generated by Django 3.2.18 on 2023-05-11 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=1)),
                ('prise_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='цена за шт.')),
                ('total_prise', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Итоговая цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='meals.order', verbose_name='Сотрудник')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='meals.product', verbose_name='Блюдо')),
            ],
            options={
                'verbose_name': 'корзина',
                'verbose_name_plural': 'корзина',
            },
        ),
    ]