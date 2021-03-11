from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Item


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()


class DetailView(generic.DetailView):
    model = Item
    template_name = 'polls/detail.html'


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
