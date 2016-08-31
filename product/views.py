from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category, Product
from django.views.generic import DetailView


def index(request):
    return HttpResponse("Product index")

class ProductDetailView(DetailView):
    
    model = Product

    def get_context_data(self, **kwargs):
    	context = super(ProductDetailView, self).get_context_data(**kwargs)
    	return context
		