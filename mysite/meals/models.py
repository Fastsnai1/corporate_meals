from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save


class Worker(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # ссылка на данный класс
        return reverse('worker', kwargs={'worker_pk': self.pk})

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'сотрудники'


class Order(models.Model):
    worker = models.ForeignKey('Worker', on_delete=models.PROTECT, null=True, verbose_name="Сотрудник")
    delivery = models.DateTimeField(verbose_name="Дата доставки")
    total_prise = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Итоговая цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return '%s # %s' % (self.worker.name, self.pk)

    def get_absolute_url(self):  # ссылка на данный класс
        return reverse('order', kwargs={'order_pk': self.pk})

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, verbose_name="Сотрудник")
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, verbose_name="Блюдо")
    num = models.IntegerField(default=1)
    prise_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="цена за шт.")
    total_prise = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Итоговая цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):  # ссылка на данный класс
        return reverse('product_in_order', kwargs={'p_in_o_pk': self.pk})

    class Meta:
        verbose_name = 'содержение закза'
        verbose_name_plural = 'содержание заказов'

    def save(self, *args, **kwargs):
        self.prise_per_item = self.product.prise
        self.total_prise = self.prise_per_item * self.num

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_product_in_order = ProductInOrder.objects.filter(order=order)
    order_total_prise = 0

    for item in all_product_in_order:
        order_total_prise += item.total_prise

    instance.order.total_prise = order_total_prise
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=400, verbose_name="Описание")
    prise = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # ссылка на данный класс
        return reverse('product', kwargs={'product_pk': self.pk})

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'блюда'


class Basket(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, verbose_name="Сотрудник", blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name="Блюдо")
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):  # ссылка на данный класс
        return reverse('basket', kwargs={'basket_id': self.pk})

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзина'

    def sum(self):
        return self.quantity * self.product.prise

