from rest_framework import serializers
from bundles.models import Bundle


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bundle
        fields = ('id', 'description', 'upc')
