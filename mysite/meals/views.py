from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *


def home(request):
    menu = Product.objects.all()
    context = {
        'menu': menu,
        'title': 'меню'
    }
    return render(request, 'meals/show_menu.html', context=context)


class Menu(ListView):
    model = Product
    template_name = 'meals/show_menu.html'  # путь к шаблону
    context_object_name = 'menu'


class ShowWorker(ListView):
    model = Worker
    template_name = 'meals/show_workers.html'  # путь к шаблону
    context_object_name = 'workers'


def histore_order(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    orders = worker.order_set.all()
    # data_orders = [p.productinorder_set.all() for p in orders]
    context = {
        'worker': worker,
        'orders': orders,
    }
    return render(request, 'meals/histore_order.html', context=context)


def add_product_in_basket(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(product=product)
    try:
        if not baskets.exists():
            Basket.objects.create(product=product, quantity=1)
            return HttpResponseRedirect(current_page)
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            return HttpResponseRedirect(current_page)

    except Exception as er:
        return HttpResponse(er)


def basket_delete(request, basket_id):
    try:
        basket = Basket.objects.get(id=basket_id)
        if basket.quantity == 1:
            basket.delete()
        else:
            basket.quantity -= 1
            basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as er:
        return HttpResponse(er)


def show_basket(request):
    baskets = Basket.objects.all()
    total_sum = sum([b.sum() for b in baskets])
    total_quantity = sum([b.quantity for b in baskets])
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            try:
                Order.objects.create(**form.cleaned_data)
                orders = Order.objects.all()
                order = orders.last()
                for basket in baskets:
                    ProductInOrder.objects.create(
                        order=order,
                        product=basket.product,
                        num=basket.quantity,
                        total_prise=total_sum,
                    )
                    basket.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except Exception as er:
                return HttpResponse(er)

    else:
        form = AddOrderForm()
        context = {
            'baskets': baskets,
            'total_quantity': total_quantity,
            'total_sum': total_sum,
            'form': form,
        }

        return render(request, 'meals/add_basket.html', context=context)


def add_order(request):
    product_in_basket = Basket.objects.all()
    form = AddOrderForm(request.POST)
    # if request.method == 'POST':

    return render(request, 'meals/show_menu.html')
