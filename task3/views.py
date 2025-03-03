from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
#введите список игр, через запитую
game = ['dandy', 'sega', 'ps1', 'ps2', 'ps3', 'тамагочи']

class home_task3(TemplateView):
    template_name = 'three_task/home_task3.html'

def market(request):
    context = {'title': 'Магазин раритетных приставок',
               'product':game
               }
    return render(request, 'three_task/market.html', context)

class cart(TemplateView):
    template_name = 'three_task/shopping_cart.html'
