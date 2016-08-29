from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category, Product
from django.views.generic.list import ListView


class IndexView(ListView):
    template_name = 'store/index.html'
    context_object_name = 'items_list'

    def get_queryset(self):
        items_list = dict(categories=Category.objects.all(),
                          products=Product.objects.all())
        return items_list
