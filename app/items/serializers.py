from rest_framework import serializers
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'item_description', 'upc', 'language')
