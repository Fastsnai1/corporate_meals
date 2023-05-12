from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    """связывает мадели внутри админки"""
    model = ProductInOrder
    extra = 0


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'created_at')  # то что видино на дисплее
    search_fields = ('created_at',)  # поля по которым можно отсортировать

    class Meta:
        model = Worker


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker', 'delivery', 'created_at')  # то что видино на дисплее
    list_display_links = ('worker', 'id')  # поля на которые можно кликнуть и перейти на соответствующию статью
    search_fields = ('created_at',)  # поля по которым можно отсортировать
    list_filter = ("worker",)  # список полей по которым можно будет фильтровать
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'num', 'total_prise', 'created_at')  # то что видино на дисплее
    list_display_links = ('order',)  # поля на которые можно кликнуть и перейти на соответствующию статью
    search_fields = ('created_at',)  # поля по которым можно отсортировать
    list_editable = ('num', 'product')  # список редактируемых полей
    list_filter = ('created_at', 'order')  # список полей по которым можно будет фильтровать

    class Meta:
        model = ProductInOrder


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'prise', 'created_at')  # то что видино на дисплее
    list_display_links = ('name',)  # поля на которые можно кликнуть и перейти на соответствующию статью
    list_editable = ('prise',)  # список редактируемых полей
    list_filter = ('created_at',)  # список полей по которым можно будет фильтровать

    class Meta:
        model = Product


class BasketAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at')
    list_display_links = ('product',)
    list_editable = ('quantity',)
    list_filter = ('created_at',)


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
