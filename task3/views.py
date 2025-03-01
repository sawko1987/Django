from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class home_task3(TemplateView):
    template_name = 'three_task/home_task3.html'

class market(TemplateView):
    template_name = 'three_task/market.html'

class cart(TemplateView):
    template_name = 'three_task/shopping_cart.html'
