from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader


from .models import Item


def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'polls/index.html', context)


def detail(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'polls/detail.html', {'item': item})
