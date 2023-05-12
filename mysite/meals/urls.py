from django.urls import path

from .views import *

urlpatterns = [
    path('', Menu.as_view(), name='home'),
    path('show_workers/', ShowWorker.as_view(), name='show_workers'),
    path('histore_order/<int:worker_id>/', histore_order, name='histore_order'),
    path('add_prod_in_basket/<int:product_id>/', add_product_in_basket, name='add_basket'),
    path('basket_delete/<int:basket_id>/', basket_delete, name='basket_delete'),
    path('show_basket/', show_basket, name='show_basket'),
    path('add_order/', add_order, name='add_order'),
]
