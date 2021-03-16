from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets

from .models import Item
from .serializers import ItemSerializer

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import io
from rest_framework.parsers import JSONParser


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'item list': 'items',
        'item detail': 'items/<int:pk>',
        'buy item': 'items/<int:pk>/buy',
        'add item': 'items/<int:pk>/add',
        'create-item': 'items/create-item'
    }
    return Response(api_urls)


class IndexView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    @action(methods=['post'], detail=False, url_path='create-item',
            url_name='create-item')
    def create_new_item(self, request):
        IndexView.create(self, request)
        return Response({'Status': '200'})

    @action(methods=['post'], detail=True, url_path='add-item',
            url_name='add-item')
    def add_item(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.quantity += 1
        item.save()
        serializer = ItemSerializer(data=item, many=False)
        serializer.is_valid()
        return Response(serializer.data)
