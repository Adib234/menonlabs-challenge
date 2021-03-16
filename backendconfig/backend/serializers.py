from backend.models import City
from rest_framework import serializers


class CurrentWeatherData(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['url', 'city']
