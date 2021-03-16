from backend.models import City
from rest_framework import viewsets
from rest_framework import permissions
from backend.serializers import CurrentWeatherData


class CurrentWeatherDataView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CurrentWeatherData
