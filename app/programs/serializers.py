from rest_framework import serializers
from programs.models import Program


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'program_id', 'program_name', 'program_type', 'retailer',
                  'retailer_item_nbr', 'program_UPC', 'season', 'year', 'status')
