from rest_framework import serializers
from holiday.models import HolliyDay

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = HolliyDay
        fields = ('user', 'id', 'hours', 'note', 'date')