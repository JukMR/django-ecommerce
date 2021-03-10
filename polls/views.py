from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


from .models import Item


def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'polls/index.html', context)


def detail(request, item_id):
    return HttpResponse(
        f"You are looking at item: {Item.objects.get(pk=item_id)}")
