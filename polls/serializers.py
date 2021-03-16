from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.description_text = (validated_data.get('description_text',
                                     instance.description_text))
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.save()
        return instance
