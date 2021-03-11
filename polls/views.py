from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Item


def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'polls/index.html', context)


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'polls/detail.html', {'item': item})


def buy_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if item.quantity > 0:
        item.quantity = item.quantity - 1
        item.save()
    else:
        return render(request, 'polls/detail.html', {
            'item': item,
            'error_message': "Product out of stock",
            })
    return HttpResponseRedirect(reverse('polls:detail', args=(item.id,)))
